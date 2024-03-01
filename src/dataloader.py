import os
import json
import torch
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset

class ImageProcessor:
    """
    A class for processing images.
    """
    def __init__(self):
        # Define transformations
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            self.normalize
        ])

    def normalize(self, tensor):
        """
        Normalize a tensor image with mean and standard deviation.
        """
        mean = torch.tensor([0.485, 0.456, 0.406]).view(-1, 1, 1)
        std = torch.tensor([0.229, 0.224, 0.225]).view(-1, 1, 1)
        return (tensor - mean) / std

    def unnormalize(self, tensor):
        """
        Unnormalize a tensor image with mean and standard deviation.
        """
        mean = torch.tensor([0.485, 0.456, 0.406]).view(-1, 1, 1)
        std = torch.tensor([0.229, 0.224, 0.225]).view(-1, 1, 1)
        return tensor * std + mean

class LabelProcessor:
    """
    A class for processing labels.
    """
    def process_labels(self, labels):
        """
        Process labels and convert points to tensors.

        Parameters:
        - labels: The labels to process.

        Returns:
        - points_tensor: The points converted to a tensor.
        """
        labels_and_points = [(label, points) for label, points in labels]
        points = [points for label, points in labels_and_points]
        points_tensor = torch.stack(points) if points else None
        return points_tensor

class OrbitImageDataset(Dataset):
    """
    A custom Dataset class for loading and processing orbit images and labels.
    """
    def __init__(self, root_dir, image_ext='.jpg', label_ext='.json'):
        """
        Initialize the dataset.

        Parameters:
        - root_dir: The directory where the images and labels are stored.
        - image_ext: The file extension for the image files.
        - label_ext: The file extension for the label files.
        """
        self.root_dir = root_dir
        self.image_ext = image_ext
        self.label_ext = label_ext
        self.json_files = [f for f in os.listdir(root_dir) if f.endswith(self.label_ext)]
        print(f"Found {len(self.json_files)} label files.")

        self.image_processor = ImageProcessor()
        self.label_processor = LabelProcessor()

    def __len__(self):
        """
        Return the number of items in the dataset.
        """
        return len(self.json_files)

    def __getitem__(self, idx):
        """
        Get an item from the dataset at a specific index.

        Parameters:
        - idx: The index of the item.

        Returns:
        - A dictionary containing the image and a list of dictionaries of labels and points.
        """
        json_file = self.json_files[idx]
        image_file = json_file.replace(self.label_ext, self.image_ext)

        # Load JSON
        with open(os.path.join(self.root_dir, json_file)) as f:
            data = json.load(f)
        labels_and_points = [{'label': shape['label'], 'points': torch.tensor(shape['points'])} for shape in data['shapes']]

        # Load image
        image = Image.open(os.path.join(self.root_dir, image_file))

        # Apply transformations to the image
        if self.image_processor.transform:
            image = self.image_processor.transform(image)

        # Identify the labels with the maximum y-coordinate
        icon_points = [item for item in labels_and_points if item['label'] == 'icon']
        digit_points = [item for item in labels_and_points if item['label'] in ['1', '2', '3', '4', '5']]

        max_icon_point = max(icon_points, key=lambda x: max(point[1] for point in x['points'])) if icon_points else None
        max_digit_point = max(digit_points, key=lambda x: max(point[1] for point in x['points'])) if digit_points else None

        # Remove the max points from the labels_and_points list
        labels_and_points = [item for item in labels_and_points if not torch.all(torch.eq(item['points'], max_icon_point['points'])) and not torch.all(torch.eq(item['points'], max_digit_point['points']))]

        return {
            'image': image,
            'labels_and_points': labels_and_points,
            'target_icon': max_icon_point,
            'target_digit': max_digit_point,
        }