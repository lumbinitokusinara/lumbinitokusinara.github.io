import os
import re
from docx2python import docx2python
from docx import Document
#import docx2txt
from bs4 import BeautifulSoup

input_folder = 'docs'
output_folder = 'docs/html'

pages_info = [
    ("page1.txt", "Section 1D F- Birth.docx", "1."),
    ("page2.txt", "Section 2 DF-Childhood Family.docx", "2."),
    ("page3.txt", "Section 3D F-Asetic life.docx", "3."),
    ("page4.txt", "Section 4 DF-Enlightenment.docx", "4."),
    ("page5.txt", "Section 5 DF- Greatness of The Buddha.docx", "5."),
    ("page6.txt", "Section 6 DF - Titles.docx", "6."),
    ("page7.txt", "Section 7 DF- As a  Teacher.docx", "7."),
    ("page8.txt", "8 Section-Praise and B.docx", "8."),
    ("page9.txt", "Section 9- DF  Past lives-.docx", "9."),
   
    ("page11_1.txt","Section 11 -1 DF- Advice to the Sangha.docx", "11.1"),
    ("page11_2.txt","Section 11-2  Advice to Lay Followers.docx", "11.2")
    
]
# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

filename = os.path.join(input_folder, "Section 4 DF-Enlightenment.docx")

# doc = docx.Document(filename)
html_content = docx2python(filename, html = True)
#print(html_content.text)

#with docx2python(filename, html = True) as html_content:
#    print(html_content.text)
    
soup = BeautifulSoup(html_content.text, "html.parser")

# Find and remove all <span> tags with a style attribute
for span in soup.find_all("span", attrs={"style": True}):
    span.unwrap()  # Removes the tag but keeps its content
    

output_path = os.path.join(output_folder,'file4.txt')
with open(output_path, "w", encoding="utf-8") as html_file:
     html_file.write(str(soup))
     html_file.close()

with open(output_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    
#modified_lines = []
firstLine = True


""" 
                stripped_line = line.strip()
                if not any(stripped_line.startswith(tag) for tag in html_tags):
                    if first_line and stripped_line:
                        outfile.write(f'<h1>{stripped_line}</h1>\n')
                        first_line = False
                    elif stripped_line.startswith('▲'):
                        outfile.write(f'<h2>{stripped_line[1:].strip()}</h2>\n')
                    elif stripped_line.startswith('♦'):
                        outfile.write(f'<h3>{stripped_line[1:].strip()}</h3>\n')
                    else:
                        outfile.write(f'<p>{stripped_line}</p>\n')
                else:
                    outfile.write(f'{stripped_line}\n') """


output_path = os.path.join(output_folder,'file4v1.txt')
with open(output_path, "w", encoding="utf-8") as html_file:
    for line in lines:
        #match = re.match(r"(endnote(\d+))\)", line.text)
        stripped_line = line.strip()
        
        stripped_line = re.sub(r'----endnote(\d+)----', r'<span id="Endnote\1">[<a href="#endnote\1">\1</a>]</span>', stripped_line)
        stripped_line = re.sub(r'endnote(\d+)\)', r'<span id="endnote\1">[<a href="#Endnote\1">\1</a>]</span>', stripped_line)
        
        if firstLine and stripped_line:
            html_file.write(f'<h1>{stripped_line}</h1>\n')
            firstLine = False
        elif stripped_line.startswith('▲'):
            html_file.write(f'<h2>{stripped_line}</h2>\n')
        elif stripped_line.startswith('♦'):
            html_file.write(f'<h3>{stripped_line}</h3>\n')
        else:                
            html_file.write(f'<p>{stripped_line}</p>\n')


#with open(output_path, "w", encoding="utf-8") as html_file:
    #html_file.write((modified_lines))

allFiles = True;
if allFiles == True:
    for ofile, docfile, section_num in pages_info:
        outputfile = os.path.join(output_folder, ofile)
        tempfile = os.path.join(output_folder, 'temp.txt')
        docfile = os.path.join(input_folder, docfile)
        print(docfile)
        page_content = docx2python(docfile, html = True)
        print(page_content.text)
        soup = BeautifulSoup(page_content.text, "html.parser")
        for span in soup.find_all("span", attrs={"style": True}):
            span.unwrap()  # Removes the tag but keeps its content
        with open(tempfile, 'w', encoding='utf-8') as temp_file:
            #print(page_file)
            temp_file.write(str(soup))
            temp_file.close()
            
        with open(tempfile, "r", encoding="utf-8") as file:
            lines = file.readlines()
            
        with open(outputfile, "w", encoding="utf-8") as html_file:
            for line in lines:
                stripped_line = line.strip()
                
                stripped_line = re.sub(r'----endnote(\d+)----', r'<span id="Endnote\1">[<a href="#endnote\1">\1</a>]</span>', stripped_line)
                stripped_line = re.sub(r'endnote(\d+)\)', r'<span id="endnote\1">[<a href="#Endnote\1">\1</a>]</span>', stripped_line)
                
                if firstLine and stripped_line:
                    html_file.write(f'<h1>{stripped_line}</h1>\n')
                    firstLine = False
                elif stripped_line.startswith('▲'):
                    html_file.write(f'<h2>{stripped_line}</h2>\n')
                elif stripped_line.startswith('♦'):
                    html_file.write(f'<h3>{stripped_line}</h3>\n')
                else:                
                    html_file.write(f'<p>{stripped_line}</p>\n')



