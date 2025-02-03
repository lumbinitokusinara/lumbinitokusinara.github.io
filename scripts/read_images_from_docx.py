import os
from docx2python import docx2python
from docx import Document
import docx2txt

input_folder = 'docs'
output_folder = 'docs/html'

pages_info = [
    ("page1.txt", "Section 1D F- Birth.docx", "page1"),
    ("page2.txt", "Section 2 DF-Childhood Family.docx", "page2"),
    ("page3.txt", "Section 3D F-Asetic life.docx", "page3"),
    ("page4.txt", "Section 4 DF-Enlightenment.docx", "page4"),
    ("page5.txt", "Section 5 DF- Greatness of The Buddha.docx", "page5"),
    ("page6.txt", "Section 6 DF - Titles.docx", "page6"),
    ("page7.txt", "Section 7 DF- As a  Teacher.docx", "page7"),
    ("page8.txt", "8 Section-Praise and B.docx", "page8"),
    ("page9.txt", "Section 9- DF  Past lives-.docx", "page9"),
   
    ("page11_1.txt","Section 11 -1 DF- Advice to the Sangha.docx", "page11_1"),
    ("page11_2.txt","Section 11-2  Advice to Lay Followers.docx", "page11_2")
]

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

filename = os.path.join(input_folder, "Section 4 DF-Enlightenment.docx")




#text = docx2txt.process(filename, output_image_folder)

page4_info = pages_info[3]
image_folder_ex = pages_info[3][0].split('.')[0]

print(image_folder_ex)
output_image_folder = os.path.join(output_folder, image_folder_ex)
os.makedirs(output_image_folder, exist_ok=True)