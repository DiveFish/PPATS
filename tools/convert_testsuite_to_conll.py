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

            for position, token in enumerate(sentence, start=0):
                # Note that an offset of 1 is added to the ID because Conll IDs start at 1.
                idx = str(position + 1)
                feats = "props:{}".format(features)

                # Note that here 0 is the starting point like in the test suite.
                if str(position) == prep_position:
                    head = int(prep_obj_position) + 1
                    current_deprel = "case"
                elif str(position) == prep_obj_position:
                    head = int(head_pos) + 1
                    current_deprel = "_"
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
