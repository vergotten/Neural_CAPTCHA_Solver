import os
import torch
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import numpy as np

from utils.circle_utils import CircleContourUtils
from dataloader import OrbitImageDataset, ImageProcessor, LabelProcessor

def collate_fn(batch):
    # batch is a list of dictionaries
    images = torch.stack([item['image'] for item in batch])
    labels_and_points = [item['labels_and_points'] for item in batch]
    target_icon = [item['target_icon'] for item in batch]
    target_digit = [item['target_digit'] for item in batch]

    return {
        'image': images,
        'labels_and_points': labels_and_points,
        'target_icon': target_icon,
        'target_digit': target_digit,
    }

def create_rectangle_patch(ax, points, label, color='r', linewidth=1):
    # Get the top-left and bottom-right points
    top_left, bottom_right = points
    # Calculate the width and height of the bounding box
    width = bottom_right[0] - top_left[0]
    height = bottom_right[1] - top_left[1]
    # Create the rectangle
    rect = patches.Rectangle(top_left, width, height, linewidth=linewidth, edgecolor=color, facecolor='none')
    ax.add_patch(rect)
    plt.text(top_left[0], top_left[1], label, color=color)

def create_circle_patch(ax, center, radius, label, color='g', linewidth=2):
    # Draw the circle on the same plot
    circle = patches.Circle(center, radius, edgecolor=color, facecolor='none', linewidth=linewidth)
    ax.add_patch(circle)
    plt.text(center[0], center[1], label, color=color)

def process_batch(i, dataloader, batch, debug=False):
    print(f'\nProcessing batch {i+1} of {len(dataloader)}')
    images = batch['image']
    labels_and_points = batch['labels_and_points']
    target_icon = batch['target_icon']
    target_digit = batch['target_digit']

    if debug:
        pprint(labels_and_points[0])
        print(f'target_icon: {target_icon[0]}')
        print(f'target_digit: {target_digit[0]}')

    return images, labels_and_points, target_icon, target_digit

def visualize_image(image, labels_and_points, target_icon, target_digit, debug=False, input_filename=None):
    # Create figure and axes
    fig, ax = plt.subplots(1)

    # Display the image
    ax.imshow(image.permute(1, 2, 0))

    # Create a Rectangle patch for each label and point
    for item in labels_and_points:
        if len(item['points']) >= 2:
            create_rectangle_patch(ax, item['points'], f'BB {item["label"]}')
        elif item['label'] == '+':
            # Assuming the radius is a constant value, for example 1
            radius = 20
            create_circle_patch(ax, item['points'][0], radius, f'Circle {item["label"]}')

    # Create a Rectangle patch for target_icon and target_digit with bold blue bounding boxes
    for j, target in enumerate([target_icon, target_digit]):
        if target is not None and len(target['points']) >= 2:
            create_rectangle_patch(ax, target['points'], f'Target {j+1}', color='y', linewidth=3)

    # Extract the base name and extension from the input filename
    base_name, ext = os.path.splitext(input_filename)
    # Append '_visGT' to the base name and reattach the extension
    output_filename = f"{base_name}_visGT{ext}"

    # Save the plot to the 'vis' directory in your root directory
    save_dir = os.path.join(os.path.dirname(os.getcwd()), 'vis/gt_vis')
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, output_filename)  # Use output_filename here
    plt.savefig(save_path)

    # Show the plot
    # plt.show()

def visualize_dataloader(dataset, num_images=None, image_ids=None, debug=False, visualize=False):
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True, collate_fn=collate_fn)

    for i, batch in enumerate(dataloader):
        # If image_ids is specified, only visualize those images
        if image_ids is not None and i not in image_ids:
            continue

        # If num_images is specified and we've visualized that many images, stop
        if num_images is not None and i >= num_images:
            break

        images, labels_and_points, target_icon, target_digit = process_batch(i, dataloader, batch, debug)

        if visualize:
            visualize_image(images[0], labels_and_points[0], target_icon[0], target_digit[0], debug, input_filename=f"image_{i}")

if __name__ == "__main__":
    # Define the path to your dataset
    dataset_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'orbits/train')

    # Initialize dataset and dataloader
    dataset = OrbitImageDataset(dataset_path)
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True, collate_fn=collate_fn)

    # Call the function with debug=True and visualize=True to print detailed information and visualize the data
    visualize_dataloader(dataset, num_images=5, debug=False, visualize=True)
