import os
import re
from docx2python import docx2python
from docx import Document
import docx2txt
from bs4 import BeautifulSoup

input_folder = 'docs'
#output_folder = 'docs/html'
output_folder = 'content'

pages_info = [
    ("Introduction.txt", "Introduction.docx", ""),
    ("page1.txt", "Section 1 - Birth.docx", "1."),
    ("page2.txt", "Section 2 - Childhood and Family of the Buddha.docx", "2."),
    ("page3.txt", "Section 3 - Asetic life.docx", "3."),
    ("page4.txt", "Section 4 - Enlightenment.docx", "4."),
    ("page4_1.txt", "Section 4-1 Four Assembly.docx", "4-1."),
    ("page5.txt", "Section 5 - Greatness of The Buddha.docx", "5."),
    ("page6.txt", "Section 6 - Titles.docx", "6."),
    ("page7.txt", "Section 7 - As a Teacher.docx", "7."),
    ("page8.txt", "Section 8 - Praise and blame.docx", "8."),
    ("page9.txt", "Section 9 - Past lives.docx", "9."),
   
    ("page11_1.txt","Section 11 -1 DF- Advice to the Sangha.docx", "11.1"),
    ("page11_2.txt","Section 11-2 Advice to Lay Followers.docx", "11.2")
    
]

html_tags = ["<html", "<head", "<body", "<div", "<span", "<script", "<style", "<p", "<a", "<ul", "<ol", "<li",
            "<table", "<tr", "<td", "<th", "<form", "<input", "<button", "<select", "<option", "<meta", "<link",
            "<pre", "<em", "<p>",
            "</html", "</head", "</body", "</div", "</span", "</script", "</style", "</p", "</a", "</ul", "</ol",
            "</li", "</table", "</tr", "</td", "</th", "</form", "</input", "</button", "</select", "</option", 
            "</h1", "</h2", "</h3", "</h4", "</h5", "</h6", "</em", "</pre", "</p>"] 

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

firstLine = True


allFiles = True;
if allFiles == True:
    for ofile, docfile, section_num in pages_info:
        image_folder_ex = ofile.split('.')[0]
        outputfile = os.path.join(output_folder, ofile)
        tempfile = os.path.join(output_folder, 'temp.txt')
        docfile = os.path.join(input_folder, docfile)
        output_image_folder = os.path.join(output_folder, image_folder_ex)
        os.makedirs(output_image_folder, exist_ok=True)
        print(output_image_folder)
        docx2txt.process(docfile, output_image_folder)
       
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
                stripped_line = re.sub(r'----media/image(\d+)\.jpeg----', lambda m: f'<img src="{image_folder_ex}/image{m.group(1)}.jpeg" />', stripped_line)
                stripped_line = re.sub(r'----media/image(\d+)\.png----', lambda m: f'<img src="{image_folder_ex}/image{m.group(1)}.png" />', stripped_line)
                stripped_line = re.sub(r'----Image alt text----&gt;.*?&lt;', '', stripped_line)
                
                
                if not any(stripped_line.startswith(tag) for tag in html_tags): 
                    if firstLine and stripped_line:
                        html_file.write(f'<h1>{stripped_line}</h1>\n')
                        firstLine = False
                    elif stripped_line.startswith('▲'):
                        html_file.write(f'<h2>{stripped_line}</h2>\n')
                    #elif stripped_line.startswith('♦'):
                    #    html_file.write(f'<h3>{stripped_line}</h3>\n')
                    else:                
                        html_file.write(f'<p>{stripped_line}</p>\n')
                else:
                    html_file.write(f'{stripped_line}\n')  



