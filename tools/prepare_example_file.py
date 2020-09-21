import argparse
import csv
import json


def create_example_template(in_file, out_file):
    with open(in_file) as f:
        reader = csv.reader(f)
        next(reader)
        meanings = [meaning for meaning in reader]

    example_template = {
        meaning[0]: {prep: ["", ""] for prep in meaning[1:]} for meaning in meanings
    }

    with open(out_file, "w") as fp:
        json.dump(example_template, fp, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("in_file", type=str, help="The input file must be in CSV format.")
    parser.add_argument("out_file", type=str, help="The output file name must have the extension '.json'.")

    args = parser.parse_args()

    create_example_template(args.in_file, args.out_file)
