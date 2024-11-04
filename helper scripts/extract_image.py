import os
import cv2

# Define directories
images_dir = "valid/images"
labels_dir = "valid/labels"
output_dir = "valid/output"

# Class name array
class_names = [
    "Green Light",
    "Red Light",
    "Speed Limit 10",
    "Speed Limit 100",
    "Speed Limit 110",
    "Speed Limit 120",
    "Speed Limit 20",
    "Speed Limit 30",
    "Speed Limit 40",
    "Speed Limit 50",
    "Speed Limit 60",
    "Speed Limit 70",
    "Speed Limit 80",
    "Speed Limit 90",
    "Stop",
]

# Create output directories for each class
for idx, class_name in enumerate(class_names):
    class_output_dir = os.path.join(output_dir, class_name)
    os.makedirs(class_output_dir, exist_ok=True)

# Get all label files
label_files = [f for f in os.listdir(labels_dir) if f.endswith(".txt")]

# Process each label file
for label_file in label_files:
    # Read the corresponding image
    image_file = label_file.replace(".txt", ".jpg")
    image_path = os.path.join(images_dir, image_file)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Image {image_file} not found.")
        continue

    img_height, img_width, _ = image.shape
    img_area = img_width * img_height

    # Read the label file
    label_path = os.path.join(labels_dir, label_file)
    with open(label_path, "r") as f:
        labels = f.readlines()

    # Process each label in the file
    for idx, label in enumerate(labels):
        label_data = label.strip().split()
        class_id = int(label_data[0])

        x_center = float(label_data[1]) * img_width
        y_center = float(label_data[2]) * img_height
        bbox_width = float(label_data[3]) * img_width
        bbox_height = float(label_data[4]) * img_height
        bbox_area = bbox_width * bbox_height

        # Check if bbox is more than 50% of the image area
        if bbox_area >= 0.5 * img_area:
            roi = image  # Save the whole image
        else:
            # Calculate new dimensions to ensure bbox is 50% of the result image
            new_bbox_width = int(bbox_width * 2)
            new_bbox_height = int(bbox_height * 2)

            # Calculate new bounding box coordinates ensuring it stays within the image
            x_min = max(0, int(x_center - new_bbox_width / 2))
            y_min = max(0, int(y_center - new_bbox_height / 2))
            x_max = min(img_width, int(x_center + new_bbox_width / 2))
            y_max = min(img_height, int(y_center + new_bbox_width / 2))

            # Extract the resized region of interest (ROI)
            roi = image[y_min:y_max, x_min:x_max]

        # Skip saving if the size of the extracted image is less than 15x15
        if roi.shape[0] < 15 or roi.shape[1] < 15:
            print(f"Skipped: bbox size {roi.shape[1]}x{roi.shape[0]} is too small.")
            continue

        # Define the output directory based on the class ID
        class_name = class_names[class_id]
        class_output_dir = os.path.join(output_dir, class_name)

        # Define the output path for the cropped image
        output_filename = (
            f"{label_file.replace('.txt', '')}_label_{class_id}_bbox_{idx}.jpg"
        )
        output_path = os.path.join(class_output_dir, output_filename)

        # Save the cropped image
        cv2.imwrite(output_path, roi)
        print(f"Saved: {output_path}")

print("Processing complete.")
