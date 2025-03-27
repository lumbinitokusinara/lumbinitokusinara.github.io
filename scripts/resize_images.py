import os
from PIL import Image

# Define the maximum width and height
MAX_WIDTH = 720
MAX_HEIGHT = 900

# Function to resize an image while maintaining aspect ratio
def resize_image(image_path, output_path):
    with Image.open(image_path) as img:
        width, height = img.size

        # Calculate scaling factors for width and height
        width_scale = MAX_WIDTH / width
        height_scale = MAX_HEIGHT / height

        # Use the most restrictive scaling factor
        scale = min(width_scale, height_scale)

        # Check if resizing is needed
        if scale < 1:
            new_width = int(width * scale)
            new_height = int(height * scale)
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            resized_img.save(output_path)
            print(f"Resized {image_path} to {new_width}x{new_height}")
        else:
            # If the image is already within the constraints, save it as is
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
           'pages/page5', 'pages/page6', 'pages/page7', 'pages/page8', 'pages/page9',
           'pages/page10', 'pages/page11', 'pages/page12', 'pages/page13',
           'pages/page13_1', 'pages/page13_2',
           'pages/page14_1', 'pages/page14_2', 'pages/page14_3',
           'pages/page15_1', 'pages/page15_2', 'pages/page15_3', 'pages/page15_4']  # Add your folder names here

# Process each folder
for folder in folders:
    print(folder)
    if os.path.exists(folder):
        process_folder(folder)
    else:
        print(f"Folder {folder} does not exist.")