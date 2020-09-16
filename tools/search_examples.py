"""

The input file must be in the same JSON format as meaning_examples.json.

Use this script in the following way:

Look for example with specific meaning and preposition:
>> python3 search_examples.py Spatial -p in

Look for all examples for one specific meaning:
>> python3 search_examples.py Spatial

Change the filename (if necessary):
>> python3 search_examples.py Spatial -p in -f other_file.json

"""

import argparse
import json


def get_example(meaning, preposition, meaning_file="material/meaning_examples.json"):
    with open(meaning_file) as ex_file:
        example_dict = json.load(ex_file)

        if example_dict.get(meaning):
            if example_dict[meaning].get(preposition):
                print(meaning + " / " + preposition + "\n")
                for example in example_dict[meaning][preposition]:
                    print(example)
            else:
                print("The preposition does not have this meaning or does not exist.")
        else:
            print("This meaning does not exist.")


def get_example_batch(meaning, meaning_file="material/meaning_examples.json"):
    with open(meaning_file) as ex_file:
        example_dict = json.load(ex_file)

    if example_dict.get(meaning):
        print(meaning + "\n")
        for prep, example_list in example_dict[meaning].items():
            print(prep + ":")
            for example in example_list:
                print(example)
            print()
    else:
        print("This meaning does not exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("meaning", type=str)
    parser.add_argument("--preposition", "-p", type=str)
    parser.add_argument("--file", "-f", type=str)

    args = parser.parse_args()

    if args.file:
        if args.preposition:
            get_example(args.meaning, args.preposition, meaning_file=args.file)
        else:
            get_example_batch(args.meaning, meaning_file=args.file)
    else:
        if args.preposition:
            get_example(args.meaning, args.preposition)
        else:
            get_example_batch(args.meaning)
