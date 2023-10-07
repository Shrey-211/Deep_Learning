import os
import shutil

# Define the source folder containing images
source_folder = "source_images"  # Change this to your source folder

# Define the destination folder where JPG images will be copied
destination_folder = "jpg_images"  # Change this to your destination folder

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file is a JPG image (case-insensitive)
    if filename.lower().endswith(".jpg"):
        # Create the full path to the source file
        source_file = os.path.join(source_folder, filename)

        # Create the full path to the destination file
        destination_file = os.path.join(destination_folder, filename)

        # Copy the file to the destination folder
        shutil.copy2(source_file, destination_file)
        print(f"Copied: {filename} to {destination_folder}")

print("Image copy process complete.")
