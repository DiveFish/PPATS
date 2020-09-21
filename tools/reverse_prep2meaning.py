import argparse
import csv


def reverse_prep_to_meaning(in_file, out_file):
    """
    A function that takes a CSV file with prepositions mapped to meanings and
    converts it to a mapping from meanings to prepositions.

    param in_file: The input file name with prep2meanings
    param outfile: The output file name with meaning2preps
    """
    with open(in_file) as inf:
        reader = csv.reader(inf)
        meaning2preps = {}

        # Take the headers out of the iterator (they are not used here).
        _headers = next(reader)

        # Iterate over the remaining lines in the CSV file.

        for line in reader:
            prep = line[0]
            # Note: The count is not needed here, so index 1 is not used.

            # Assign prepositions to meanings.
            for meaning in line[2:]:
                if meaning2preps.get(meaning):
                    meaning2preps[meaning].append(prep)
                else:
                    meaning2preps[meaning] = [prep]

    with open(out_file, "w") as outf:
        writer = csv.writer(outf)

        # Get maximum number of prepositions per meaning to set the number
        # of columns.
        max_num_preps = max(map(len, meaning2preps.values()))

        # Write header row.
        writer.writerow(
            ["meaning"] + ["preposion" + str(n) for n in range(1, max_num_preps + 1)]
        )

        # Write meaning and prepositions to file.
        for meaning, preps in meaning2preps.items():
            writer.writerow([meaning] + preps)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "in_file",
        type=str,
        help="The input file must be in CSV format. "
        "The file prep2meaning.csv serves as example.",
    )
    parser.add_argument(
        "out_file", type=str, help="The output file must be in CSV format."
    )

    args = parser.parse_args()

    reverse_prep_to_meaning(args.in_file, args.out_file)
