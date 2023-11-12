# TODO импортировать необходимые молул
from csv import DictReader
from json import dump

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task(csv_file_path, json_file_path, values_separator=",", lines_separator="\n") -> None:
    json_data = []
    with open(csv_file_path, "r") as f:
        csv_reader = DictReader(f, delimiter=values_separator, quotechar=lines_separator)
        for line in csv_reader:
            json_data.append(line)
    with open(json_file_path, "w") as f:
        dump(json_data, f, indent=4)

if __name__ == '__main__':
    task(INPUT_FILENAME, OUTPUT_FILENAME)
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")










