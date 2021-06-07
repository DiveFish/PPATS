import csv
import sys


def testsuite_to_conll(testsuite_file, conll_file):
    with open(testsuite_file) as testsuite, open(conll_file, "w") as conll:
        reader = csv.reader(testsuite, delimiter="\t")
        writer = csv.writer(conll, delimiter= "\t")

        # Get rid of header in file.
        _ = next(reader)

        for line in reader:
            features = line[0]
            prep_position = line[2]
            prep_obj_position = line[3]
            head_pos = line[4]
            deprel = line[5]
            sentence = line[6].split()
            # TODO: Following 4 lines can be removed once a space is added before the dot in the suite.
            last_token = sentence.pop(-1)
            last_word = last_token[:-1]
            dot = last_token[-1]
            sentence.extend([last_word, dot])

            for position, token in enumerate(sentence, start=0):
                # Note that an offset of 1 is added to the ID because Conll IDs start at 1.
                idx = str(position + 1)
                feats = "props:{}".format(features)

                # Note that here 0 is the starting point like in the test suite.
                if str(position) == prep_position:
                    head = prep_position
                    current_deprel = "case"
                elif str(position) == prep_obj_position:
                    head = prep_obj_position
                    current_deprel = deprel
                else:
                    head = "_"
                    current_deprel = "_"

                conll_line = [idx, token, "_", "_", "_", feats, head, current_deprel, "_", "_"]
            
                writer.writerow(conll_line)
            writer.writerow([])


if __name__ == "__main__":
    testsuite_file = sys.argv[1]
    conll_file = sys.argv[2]

    testsuite_to_conll(testsuite_file, conll_file)
