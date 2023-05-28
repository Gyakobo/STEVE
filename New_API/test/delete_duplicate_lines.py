def remove_duplicate_lines(file_path):
    lines_seen = set()  # Set to store unique lines
    updated_lines = []  # List to store unique lines in order

    # Read the file and filter out duplicate lines
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line not in lines_seen:
                lines_seen.add(line)
                updated_lines.append(line)

    # Write the unique lines back to the file
    with open(file_path, 'w') as file:
        file.write('\n'.join(updated_lines))


# Usage example
file_path = '/home/andrew/STEVE/New_API/inputfile.txt'  # Replace with your file path
remove_duplicate_lines(file_path)