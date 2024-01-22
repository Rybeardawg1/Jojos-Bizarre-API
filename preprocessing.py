import re


def remove_dashes_and_hyphens(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()

    # Remove dashes and hyphens
    cleaned_content = content.replace("-", "").replace("—", "").replace("–", "")

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(cleaned_content)


def remove_single_letter_lines(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()

    # Remove single letter lines
    cleaned_content = "\n".join([line for line in content.split("\n") if len(line) > 1])

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(cleaned_content)


def remove_text_before_colon(input_file, output_file, start_line=14299):
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    # Remove text before the first colon from the specified line
    for i in range(start_line - 1, len(lines)):
        line = lines[i]
        colon_index = line.find(":")
        if colon_index != -1:
            lines[i] = line[colon_index + 1 :]

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.writelines(lines)


def remove_bracket_content(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    # Remove content within curly brackets
    cleaned_lines = [re.sub(r"\{.*?\}", "", line) for line in lines]

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.writelines(cleaned_lines)


# Replace 'input.txt' and 'output.txt' with your file names
remove_bracket_content("data.txt", "output.txt")
