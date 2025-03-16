import os
from docx2python import docx2python
from docx import Document
import docx2txt

input_folder = 'docs'
output_folder = 'docs/html'

pages_info = [
    ("Introduction.txt", "Introduction-.docx", ""),
    ("page1.txt", "Section 1-Birth.docx", "1."),
    #("page1.txt", "1 - Birth of the Buddha Gotama.docx", "1."),
    ("page2.txt", "Section 2- Childhood and Family of the Buddha.docx", "2."),
    ("page3.txt", "Section 3-Asetic life.docx", "3."),
    ("page4.txt", "Section 4 -Enlightenment.docx", "4."),
    ("page4_1.txt", "Section 4-1 Four Assembly.docx", "4-1."),
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

filename = os.path.join(input_folder, "Section 4 -Enlightenment.docx")




#text = docx2txt.process(filename, output_image_folder)

page4_info = pages_info[3]
image_folder_ex = pages_info[3][0].split('.')[0]

print(image_folder_ex)
output_image_folder = os.path.join(output_folder, image_folder_ex)
os.makedirs(output_image_folder, exist_ok=True)