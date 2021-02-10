import csv
import os
import sys


def num_prep_meaning(dir_name, table_file, prep2mean_topf, mean2prep_topf):
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

    top_num_prep2meaning(preps, prep2mean_topf, mean2prep_topf, )

    with open(table_file, "w") as outf:
        writer = csv.writer(outf, delimiter="\t")
        writer.writerow(["prep"] + list(meaning_map.keys()))

        for prep, meanings in preps.items():
            line_out = [prep] + [0] * len(meaning_map)
            for meaning, num in meanings.items():
                line_out[meaning_map[meaning] + 1] = num

            writer.writerow(line_out)


def top_num_prep2meaning(preps, prep2mean_topf, mean2prep_topf):
    with open(prep2mean_topf, "w") as p2mtopf, open(mean2prep_topf, "w") as m2ptopf:
        p2m_writer = csv.writer(p2mtopf)
        m2p_writer = csv.writer(m2ptopf)

        meaning_dict = {}

        preps = dict(sorted(preps.items(), key=lambda x: x[0]))

        for prep, meanings in preps.items():
            # Set up top meanings per preposition.
            current_line = [prep]
            top_sorted = sorted(meanings.items(), key=lambda x: x[1], reverse=True)
            for meaning, num in top_sorted[:5]:
                current_line.append((meaning, num))

            for meaning, num in top_sorted:
                # Set up top prepositions per meanings.
                if meaning_dict.get(meaning):
                    meaning_dict[meaning].append((prep, num))
                else:
                    meaning_dict[meaning] = [(prep, num)]

            p2m_writer.writerow(current_line)

        # Sort alphabetically
        meaning_dict = dict(sorted(meaning_dict.items(), key=lambda x: x[0]))

        for meaning, prep_num_list in meaning_dict.items():
            current_line = [meaning]
            top_sorted = sorted(prep_num_list, key=lambda x: x[1], reverse=True)
            for prep, num in top_sorted:
                current_line.append((prep, num))
            m2p_writer.writerow(current_line)


if __name__ == "__main__":
    dir_name = sys.argv[1]
    out_file = sys.argv[2]
    prep2mean_topf = sys.argv[3]
    mean2prep_topf = sys.argv[4]

    num_prep_meaning(dir_name, out_file, prep2mean_topf, mean2prep_topf)
