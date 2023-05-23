import os

def merge_dedup(directory, output_file):
    all_values = set()

    for filename in os.listdir(directory):
        print('Processing file: ' + filename)
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    value = line.strip()
                    all_values.add(value)

    filtered_values = list(all_values)

    with open(output_file, 'w') as file:
        for value in filtered_values:
            file.write(value + '\n')

input_directory = './input'
output_file = 'filtered.txt'
merge_dedup(input_directory, output_file)
