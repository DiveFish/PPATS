import csv
import sys


def testsuite_to_conll(conllx_file):
    """
    Convert a Conll-X file to a Conll-U file.
    The name of the Conll-U file is equal to the Conll-X file name with
    a "_u" add between basename and extension.

    example.conll -> example_u.conll
    """
    path, extension = conllx_file.split(".")
    conllu_file = path + "_u." + extension

    with open(conllx_file) as conllx, open(conllu_file, "w") as conllu:
        reader = csv.reader(conllx, delimiter="\t")
        writer = csv.writer(conllu, delimiter="\t")

        for line in reader:
            if line:
                line[5] = line[5].replace(":", "=")

            writer.writerow(line)


if __name__ == "__main__":
    conllx_file = sys.argv[1]

    testsuite_to_conll(conllx_file)