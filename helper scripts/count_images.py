import os

# Define paths to the directories
train_dir = "Road_Sign_Classification_Dataset/train"
valid_dir = "Road_Sign_Classification_Dataset/valid"
test_dir = "Road_Sign_Classification_Dataset/test"


# Function to count images in a directory
def count_images_in_directory(directory):
    class_counts = {}
    total_count = 0

    # Iterate over each class directory
    for class_name in os.listdir(directory):
        class_path = os.path.join(directory, class_name)

        if os.path.isdir(class_path):
            # Count the number of images in this class directory
            num_images = len(
                [
                    img
                    for img in os.listdir(class_path)
                    if img.endswith(("jpg", "jpeg", "png"))
                ]
            )
            class_counts[class_name] = num_images
            total_count += num_images

    return class_counts, total_count


# Count images in each split
train_counts, total_train = count_images_in_directory(train_dir)
valid_counts, total_valid = count_images_in_directory(valid_dir)
test_counts, total_test = count_images_in_directory(test_dir)

# Print out the results
print("Train Set:")
for class_name, count in train_counts.items():
    print(f"{class_name}: {count} images")
print(f"Total: {total_train} images\n")

print("Validation Set:")
for class_name, count in valid_counts.items():
    print(f"{class_name}: {count} images")
print(f"Total: {total_valid} images\n")

print("Test Set:")
for class_name, count in test_counts.items():
    print(f"{class_name}: {count} images")
print(f"Total: {total_test} images\n")
