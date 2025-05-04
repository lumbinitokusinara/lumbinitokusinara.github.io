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
    ("Introduction.txt", "Introduction.docx", "II."),
   # ("Acknowledgements.txt", "Acknowledgements.docx", "IV."),
   # ("page1.txt", "Section 1 - Birth.docx", "1."),
    ("page2.txt", "Section 2 - Childhood and Family of the Buddha.docx", "2."),
   # ("page3.txt", "Section 3 - Asetic life.docx", "3."),
   # ("page4.txt", "Section 4 - Enlightenment.docx", "4."),
   # ("page4_1.txt", "Section 4-1 Four Assembly.docx", "4-1."),
   # ("page5.txt", "Section 5 - Greatness of The Buddha.docx", "5."),
  #  ("page6.txt", "Section 6 - Titles.docx", "6.")
  #  ("page7.txt", "Section 7 - As a Teacher.docx", "7."),
   # ("page8.txt", "Section 8 - Praise and blame.docx", "8."),
  #  ("page9.txt", "Section 9 - Past lives.docx", "9."),
  #  ("page10.txt", "Section 10 - Dhamma.docx", "10."),
  #  ("page11_1.txt","Section 11-1 Advice to the Sangha.docx", "11.1"),
  #  ("page11_2.txt","Section 11-2 Advice to Lay Followers.docx", "11.2"),
  #  ("page12.txt","Section 12 - Similies.docx", "12."),
  #  ("page13.txt","Section 13 - Introduction- 45 years of life of the Buddhas.docx", "13."),
  #  ("page13_1.txt","Section 13-1 First Dhamma Tour-45.docx", "13.1"),
  #  ("page13_2.txt","Section 13-2 Second Dhamma Tour.docx", "13.2"),
   # ("page14_1.txt","Section 14-1 The Buddha Meets King Seniya Bimbisāra of Magadha.docx", "14.1"),
   # ("page14_2.txt","Section 14-2 Fourth and Fifth Walking Tours.docx", "14.2"),
   # ("page14_3.txt","Section 14-3 Second to Fourth Vassa Spent in Rājagaha (Age 36-39).docx", "14.3"),
   # ("page15_1.txt","Section 15-1 Fifth Vassa Spent in Vesālȋ (Age 39).docx", "15.1"),
   # ("page15_2.txt","Section 15-2 Sixth to Eighth Vassa- Age 40 - 42 Years.docx", "15.2"),
   # ("page15_3.txt","Section 15-3 Ninth to Tenth Vassa (Age 43 - 44).docx", "15.3"),
   # ("page15_4.txt","Section 15-4 Eleventh and Twelfth Vassa (Age 45 to 46).docx", "15.4"),
   # ("page16_1.txt","Section 16-1 Thirteenth, Fourteenth and Fifteenth Vassa (Age 47 to 49).docx", "16.1"), 
   # ("page16_2.txt","Section 16-2 Sixteenth to Seventeenth Vassa (Age 50-51).docx", "16.2"),
   # ("page16_3.txt","Section 16-3 Eighteenth to Nineteenth Vassa (Age 52-53).docx", "16.3"),
   # ("page17.txt","Section 17 - Twentieth Vassa (Age 54-55).docx", "17."),   
   # ("page18.txt","Section 18 - Twenty-first to Forty-fourth Vassa in Savatthi (from Age 55 onwards).docx", "18."),
   # ("page19_1.txt","Section 19-1 Final Journey of The Buddha Phase 1.docx  ", "19.1"),   
   # ("page19_2.txt","Section 19-2 Final Journey of The Buddha Phase 2.docx  ", "19.2"),  
   # ("page19_3.txt","Section 19-3 Final Journey of The Buddha Phase 3.docx  ", "19.3"),  
   # ("page19_4.txt","Section 19-4 Final Journey of The Buddha Phase 4.docx  ", "19.4"),  
   #("page19_5.txt","Section 19-5 Final Journey of The Buddha Phase 5.docx  ", "19.5"),  
    ("page19_6.txt","Section 19-6 The Funeral of the Blessed One.docx", "19.6"),
    ("Appendix.txt","Appendix.docx", "Appendix to Section 19.6")    
  #  ("Gratitude.txt","Gratitude to the Blessed One.docx", "III."),
  #  ("Abbreviations.txt","Abbreviations.docx", "V.")
    
]

html_tags = ["<html", "<head", "<body", "<div", "<span", "<script", "<style", "<p", "<ul", "<ol", "<li",
            "<table", "<tr", "<td", "<th", "<form", "<input", "<button", "<select", "<option", "<meta", "<link",
            "<pre", "<em", "<p", "<h1", "<h2", "<h3", "<h4", "<h5", "<h6", "<img", "<br", "<hr", "<!--", "<title",
            "</html", "</head", "</body", "</div", "</span", "</script", "</style", "</p",  "</ul", "</ol",
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
        # extract images
        docx2txt.process(docfile, output_image_folder)
       
        print(docfile)
        page_content = docx2python(docfile, html = True)
        #print(page_content.text)
        soup = BeautifulSoup(page_content.text, "html.parser")
        for span in soup.find_all("span", attrs={"style": True}):
            span.unwrap()  # Removes the tag but keeps its content
        with open(tempfile, 'w', encoding='utf-8') as temp_file:
            #print(page_file)
            temp_file.write(str(soup))
            temp_file.close()
        
        FirstLine = True   
        with open(tempfile, "r", encoding="utf-8") as file:
            lines = file.readlines()
            
        with open(outputfile, "w", encoding="utf-8") as html_file:
            html_file.write(f'<div class="container">\n')
            html_file.write(f'<article class="pagewidth">\n')
            capture_next = False
            capture_next_now = False
            for line in lines:
                stripped_line = line.strip()
                #print(stripped_line)
                if re.match(r'----media/.*\.(jpeg|jpg|gif|png)----', stripped_line):
                    capture_next = True
                    capture_next_now = True
                    print('Image line detected ............')
                    print(stripped_line)
                    #outfile.write(line)  # Write the media line as is
                    #continue
                
                stripped_line = re.sub(r'----endnote(\d+)----', r'<span id="Endnote\1">[<a href="#endnote\1">\1</a>]</span>', stripped_line)
                stripped_line = re.sub(r'endnote(\d+)\)', r'<span id="endnote\1">[<a href="#Endnote\1">\1</a>]</span>', stripped_line)
                stripped_line = re.sub(r'----media/image(\d+)\.jpeg----', lambda m: f'<img src="{image_folder_ex}/image{m.group(1)}.jpeg" />', stripped_line)
                stripped_line = re.sub(r'----media/image(\d+)\.gif----', lambda m: f'<img src="{image_folder_ex}/image{m.group(1)}.gif" />', stripped_line)
                stripped_line = re.sub(r'----media/image(\d+)\.png----', lambda m: f'<img src="{image_folder_ex}/image{m.group(1)}.png" />', stripped_line)
                stripped_line = re.sub(r'----Image alt text----&gt;.*?&lt;', '', stripped_line)
                
                
                if capture_next_now:
                    print(stripped_line)
                
                if not any(stripped_line.startswith(tag) for tag in html_tags): 
                    if firstLine and stripped_line:
                        html_file.write(f'<h1>{stripped_line}</h1>\n')
                        firstLine = False
                    
                    
                    
                    elif capture_next and stripped_line:
                        # Check if the line does not contain HTML header tags
                        print(stripped_line.encode("utf-8"))
                        if not re.search(r'<(h1|h2|h3|h4|h5|h6)[^>]*>', stripped_line, re.IGNORECASE):
                            # Enclose the line in <p class="caption"> </p>
                            html_file.write(f'<p class="caption">{stripped_line}</p>\n')
                        else:
                            # If it contains header tags, write it as is
                            html_file.write(line)
                        capture_next = False
                   
                    
                    elif stripped_line.startswith('▲'):
                        html_file.write(f'<h2>{stripped_line}</h2>\n')
                    #elif stripped_line.startswith('♦'):
                    #    html_file.write(f'<h3>{stripped_line}</h3>\n')
                    else:                
                        html_file.write(f'<p>{stripped_line}</p>\n')
                else:
                    
                    html_file.write(f'{stripped_line}\n')  
                    if capture_next_now:
                        print(f'****** {stripped_line}')
                        capture_next_now = False
                    else:    
                        capture_next = False
                        
            html_file.write(f'</article>\n')
            html_file.write(f'</div>\n')



