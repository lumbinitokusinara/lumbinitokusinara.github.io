# generate_json.py
import os
import json

# Path to the content folder
content_folder = "content"
pages_folder = "pages"

# Dictionary to store content
content_data = {}

# Loop through all .txt files in the content folder
for filename in os.listdir(content_folder):
    
    if filename.endswith(".txt"):
        print(filename)
        # Extract the page name (e.g., "page1" from "page1.txt")
        page_name = filename.split(".")[0]
        
        # Read the content of the file
        with open(os.path.join(content_folder, filename), "r", encoding="utf-8") as file:
            content = file.read()
        
        # Add the content to the dictionary
        content_data[page_name] = content

# Write the dictionary to a JSON file
with open("pages/content.json", "w", encoding="utf-8") as json_file:
    json.dump(content_data, json_file, indent=4)

print("content.json generated successfully!")