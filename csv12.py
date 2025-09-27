# filename: csv_to_key_value.py

import csv

def csv_to_key_value(input_file, output_file="output.txt"):
    """Reads a CSV and writes key-value pairs of headers and row values."""
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        first_row = next(reader, None)  # only take the first row
    
    if first_row:
        with open(output_file, "w", encoding="utf-8") as out:
            for key, value in first_row.items():
                line = f"{key}: {value}"
                print(line)         # print to console
                out.write(line + "\n")  # save to file

if __name__ == "__main__":
    csv_to_key_value("input.csv")
