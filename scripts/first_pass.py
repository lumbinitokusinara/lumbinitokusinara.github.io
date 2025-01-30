import os

input_folder = 'content/unsorted'
output_folder = 'content/firstpass'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each .txt file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
            first_line = True
            for line in infile:
                stripped_line = line.strip()
                if first_line and stripped_line:
                    outfile.write(f'<h1>{stripped_line}</h1>\n')
                    first_line = False
                elif stripped_line.startswith('▲'):
                    outfile.write(f'<h2>{stripped_line[1:].strip()}</h2>\n')
                elif stripped_line.startswith('♦'):
                    outfile.write(f'<h3>{stripped_line[1:].strip()}</h3>\n')
                else:
                    outfile.write(f'<p>{stripped_line}</p>\n')