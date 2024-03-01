import cv2
import numpy as np


class CircleContourUtils:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def find_circle_contours(self):
        _, thresh = cv2.threshold(self.gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def highlight_circle_segment(self, point_coordinates, radius=20):
        result_img = self.image.copy()
        center = tuple(map(int, point_coordinates))
        cv2.circle(result_img, center, radius, (0, 255, 0), 2)
        return result_img, center, radius

    def is_point_in_patch(self, point, center, radius):
        # Calculate the distance between the point and the center of the circle
        distance = np.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)

        # If the distance is less than or equal to the radius, the point is inside the circle
        return distance <= radius


# if __name__ == "__main__":
#     dataiter = iter(dataloader)
#
#     # Get the next batch
#     batch = next(dataiter)
#
#     image = batch['image'][0]
#     first_labels = batch['labels_and_points'][0]
#     filtered_labels_and_points = [item for item in first_labels if item['label'] == '+' or len(item['points']) == 1]
#
#     # Convert the tensor to a numpy array
#     image_np = image.permute(1, 2, 0).numpy()
#
#     # Normalize the values to the range 0-1
#     # image_np = (image_np + 1) / 2
#
#     # Normalize the values to the range 0-1
#     image_np = (image_np - image_np.min()) / (image_np.max() - image_np.min())
#
#     # Print the min and max of the normalized image
#     print(f"Normalized image min: {image_np.min()}, max: {image_np.max()}")
#
#     # Convert the numpy array to an image file
#     cv2.imwrite("single_image.jpg", (image_np * 255).astype(np.uint8))
#
#     # Now you can pass the image file to the CircleContourUtils class
#     utils = CircleContourUtils("single_image.jpg")
#
#     # Highlight the circle segment for each point
#     for i, item in enumerate(filtered_labels_and_points):
#         point = item['points'][0].numpy()  # Assuming each item has at least one point
#         result_img, circle_center, circle_radius = utils.highlight_circle_segment(point)
#
#         print(f"Point coordinates: {point}")
#         print(f"Circle patch coordinates: Center - {circle_center}, Radius - {circle_radius}")
#
#         # Check if the point is in the patch
#         if utils.is_point_in_patch(point, circle_center, circle_radius):
#             print("The point is in the patch.")
#         else:
#             print("The point is not in the patch.")
#
#         # Convert the image from BGR to RGB
#         result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
#
#         # Print the shape and type of the result image
#         print(f"Result image shape: {result_img_rgb.shape}, type: {result_img_rgb.dtype}")
#
#         # Display the result
#         cv2_imshow(result_img_rgb)