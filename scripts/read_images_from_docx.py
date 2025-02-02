import os
from docx2python import docx2python
from docx import Document
import docx2txt

input_folder = 'docs'
output_folder = 'docs/images'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

filename = os.path.join(input_folder, "Section 4 DF-Enlightenment.docx")

# doc = docx.Document(filename)
h1 = docx2python(filename, html = True)

with docx2python(filename, html = True) as html_content:
    print(html_content.text)
    

print(html_content.body)

hc1 = ''

for para in html_content.body:
    hc1 += f"{para}\n"
# text = docx2txt.process(filename)

# print(text)

# text = docx2txt.process(filename, output_folder)

output_path = os.path.join(output_folder,'file4.html')
with open(output_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_content.text)

# for filename in os.listdir(input_folder):
#     if filename.endswith('.docx'):
#         input_path = os.path.join(input_folder, filename)
#         output_filename = os.path.splitext(filename)[0] + ".html"
        
#         output_path = os.path.join(output_folder, output_filename)
        
#         doc = Document(input_path)
        
#         html_content = ''
#             # Convert each paragraph to a <p> tag
#         for para in doc.paragraphs:
#             html_content += f"<p>{para.text}</p>\n"
        
#         # print(html_content)
        
#         print(input_path)
      
#         with open(output_path, "w", encoding="utf-8") as html_file:
#             html_file.write(html_content)