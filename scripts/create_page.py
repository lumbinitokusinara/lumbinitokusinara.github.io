import os

# Define the titles and section numbers
pages_info = [
    ("page1.html", "1. Birth of the Buddha", "1."),
    ("page2.html", "2. Childhood and Family Life", "2."),
    ("page3.html", "3. Ascetic Life", "3."),
    ("page4.html", "4. Enlightenment", "4."),
    ("page4_1.html", "4.1. Establishment of the Community", "4.1"),
    ("page5.html", "5. The Greatness of the Buddha", "5."),
    ("page6.html", "6. Titles and Epithets for the Buddha", "6."),
    ("page7.html", "7. Buddha as the Teacher", "7."),
    ("page8.html","8. Receiving Praise and Blame", "8."),
    ("page9.html","9. Past Lives of the Buddha", "9."),
    ("page10.html","10. Significant Dhamma Teachings", "10."),
    ("page11_1.html","11.1 Advice and Guidance to the Sangha", "11.1"),
    ("page11_2.html","11.2 Advice and Guidance to Lay Followers", "11.2"),
    ("page12.html","12. Similes- Metaphors of the Buddha", "12"),
    ("page13.html","13. Introduction of 45 years of Buddha's life", "13"),
    ("page13_1.html","13.1 First Dhamma Tour to 1st Rain season", "13.1"),
    ("page13_2.html","13.2 2nd Dhamma tour to the 3rd tour", "13.2"),
    ("page14_1.html","14.1 Events occurred at Rajagha", "14.1"),
    ("page14_2.html","14.2 Fourth Dhamma Tour to Kapilvattu", "14.2"),
    ("page15.html","15. Fifth Vassa to 45th Vassa", "15")
]

# Read the template file with UTF-8 encoding
with open('scripts/page_template.html', 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()

# Create the pages directory if it doesn't exist
os.makedirs('pages', exist_ok=True)

# Generate the pages
for filename, title, section_num in pages_info:
    page_content = template_content.replace('$Title$', title).replace('$SectionNum$', section_num)
    with open(os.path.join('pages', filename), 'w', encoding='utf-8') as page_file:
        print(page_file)
        page_file.write(page_content)

print("Pages created successfully.")