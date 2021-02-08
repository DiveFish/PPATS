import csv
import os
import sys


def num_prep_meaning(dir_name, out_file):
    preps = {}
    meanings = set()

    for csv_file in os.listdir(dir_name):
        if csv_file.endswith(".csv"):
            path = os.path.join(dir_name, csv_file)
            with open(path) as f:
                prep = os.path.splitext(csv_file)[0]
                preps[prep] = {}
                reader = csv.reader(f)
                meaning_col = 7 if prep == "in" else 34
                for line in reader:
                    meaning = line[meaning_col].strip()
                    meanings.add(meaning)

                    if preps[prep].get(meaning):
                        preps[prep][meaning] += 1
                    else:
                        preps[prep][meaning] = 1

    meaning_map = {meaning: num for meaning, num in zip(meanings, range(len(meanings)))}

    with open(out_file, "w") as outf:
        writer = csv.writer(outf, delimiter="\t")
        writer.writerow(["prep"] + list(meaning_map.keys()))

        for prep, meanings in preps.items():
            line_out = [prep] + [0] * len(meaning_map)
            for meaning, num in meanings.items():
                line_out[meaning_map[meaning] + 1] = num

            writer.writerow(line_out)


if __name__ == "__main__":
    dir_name = sys.argv[1]
    out_file = sys.argv[2]

    num_prep_meaning(dir_name, out_file)