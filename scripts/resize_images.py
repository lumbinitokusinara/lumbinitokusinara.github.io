import os
from PIL import Image

# Define the maximum width
MAX_WIDTH = 720

# Function to resize an image while maintaining aspect ratio
def resize_image(image_path, output_path):
    with Image.open(image_path) as img:
        # Calculate the new height to maintain the aspect ratio
        width, height = img.size
        if width > MAX_WIDTH:
            new_height = int((MAX_WIDTH / width) * height)
            resized_img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
            resized_img.save(output_path)
            print(f"Resized {image_path} to {MAX_WIDTH}x{new_height}")
        else:
            # If the image is already 720px or less in width, just save it as is
            img.save(output_path)
            print(f"No resizing needed for {image_path}")

# Function to process all images in a folder
def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                image_path = os.path.join(root, file)
                output_path = os.path.join(root, file)  # Overwrite the original image
                resize_image(image_path, output_path)

# List of folders to process
folders = ['pages/page1', 'pages/page2', 'pages/page3','pages/page4', 'pages/page4_1',
           'pages/page5', 'pages/page6', 'pages/page7', 'pages/page8', 'pages/page9']  # Add your folder names here

# Process each folder
for folder in folders:
    print(folder)
    if os.path.exists(folder):
        process_folder(folder)
    else:
        print(f"Folder {folder} does not exist.")