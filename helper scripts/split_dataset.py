from sklearn.model_selection import train_test_split
import os
import shutil
import glob

# Define the paths
dataset_dir = "helper datasets/All_Images_Dataset"
train_dir = "Road_Sign_Classification_Dataset/train"
valid_dir = "Road_Sign_Classification_Dataset/valid"
test_dir = "Road_Sign_Classification_Dataset/test"

# Create directories for train, validation, and test datasets
os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Class names based on the folders
classes = ["GiveWay", "NoEntry", "SpeedLimit", "Stop"]

# Create subdirectories for each class in train, validation, and test directories
for class_name in classes:
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(valid_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)


# Function to split data into train, validation, and test sets
def split_data(class_name):
    class_path = os.path.join(dataset_dir, class_name)
    images = (
        glob.glob(os.path.join(class_path, "*.jpg"))
        + glob.glob(os.path.join(class_path, "*.jpeg"))
        + glob.glob(os.path.join(class_path, "*.png"))
    )

    print(
        f"Class: {os.path.join(dataset_dir, class_name)}, Number of images: {len(images)}"
    )
    train_images, test_images = train_test_split(images, test_size=0.4, random_state=42)
    test_images, valid_images = train_test_split(
        test_images, test_size=0.5, random_state=42
    )

    # Copy the images to the respective directories
    for img in train_images:
        shutil.copy(img, os.path.join(train_dir, class_name))

    for img in valid_images:
        shutil.copy(img, os.path.join(valid_dir, class_name))

    for img in test_images:
        shutil.copy(img, os.path.join(test_dir, class_name))


# Split data for each class
for class_name in classes:
    split_data(class_name)
