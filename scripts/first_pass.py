import os

input_folder = 'content/unsorted'
output_folder = 'content'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each .txt file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if line.startswith('▲'):
                    outfile.write(f'<h2>{line[1:].strip()}</h2>\n')
                elif line.startswith('♦'):
                        outfile.write(f'<h3>{line[1:].strip()}</h3>\n')
                else:
                    outfile.write(f'<p>{line.strip()}</p>\n')

                