# Generate the pages
for filename, title, section_num in pages_info:
    page_content = template_content.replace('$Title$', title).replace('$SectionNum$', section_num)
    with open(os.path.join('pages', filename), 'w', encoding='utf-8') as page_file:
        print(page_file)
        page_file.write(page_content)