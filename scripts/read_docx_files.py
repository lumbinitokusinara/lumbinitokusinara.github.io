import os
import docx
from docx import Document

input_folder = 'docs'
output_folder = 'docs/html'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.docx'):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".html"
        
        output_path = os.path.join(output_folder, output_filename)
        
        doc = Document(input_path)
        
        html_content = ''
            # Convert each paragraph to a <p> tag
        for para in doc.paragraphs:
            html_content += f"<p>{para.text}</p>\n"
        
        # print(html_content)
        
        print(input_path)
      
        with open(output_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)