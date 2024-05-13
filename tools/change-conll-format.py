import argparse
import csv


def convert_conll(conll_file, direction):
    """
    Convert a Conll-X file to a Conll-U file and vice versa.
    The name of the Conll-U file is equal to the Conll-X file name with
    a "_u" add between basename and extension.

    Conll-X to Conll-U: example.conll -> example_u.conll
    Conll-U to Conll-X: example_u.conll -> example.conll

    :param conll_file: The name of the conll_file.
    :param direction: The value determines whether to convert to Conll-X or Conll-U.
    """
    if direction == "u":
        path, extension = conll_file.split(".")
        target_file = path + "_u." + extension
    elif direction == "x":
        assert "_u" in conll_file, "For a conversion from Conll-X to Conll-U the basename must end in '_u'."
        path, extension = conll_file.split(".")
        target_file = path[:-2] + "." + extension
        
    with open(conll_file) as conll, open(target_file, "w") as target:
        reader = csv.reader(conll, delimiter="\t")
        writer = csv.writer(target, delimiter="\t")

        for line in reader:
            if line:
                if direction == "u":
                    line[5] = line[5].replace(":", "=")
                elif direction == "x":
                    line[5] = line[5].replace("=", ":")

            writer.writerow(line)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()

    argparser.add_argument("conll_file", type=str)
    conll_types = argparser.add_mutually_exclusive_group()
    conll_types.add_argument("--to_conllu", "-u", action="store_true")
    conll_types.add_argument("--to_conllx", "-x", action="store_true")

    args = argparser.parse_args()

    if args.to_conllu:
        convert_conll(args.conll_file, "u")
    elif args.to_conllx:
        convert_conll(args.conll_file, "x")
