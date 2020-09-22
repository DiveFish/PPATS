"""

The input file must be in the same JSON format as meaning_examples.json.

Use this script in the following way:

Look for example with specific meaning and preposition:
>> python3 search_examples.py -m Spatial -p in

Look for all examples for one specific meaning:
>> python3 search_examples.py -m Spatial

Look for all examples for one specific preposition:
>> python3 search_examples.py -p in

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


def get_examples_meaning(meaning, meaning_file="material/meaning_examples.json"):
    with open(meaning_file) as ex_file:
        example_dict = json.load(ex_file)

    if example_dict.get(meaning):
        print("Meaning: " + meaning + "\n")
        for prep, example_list in example_dict[meaning].items():
            print("[" + prep + "]")
            for example in example_list:
                print(example)
            print()
    else:
        print("This meaning does not exist.")


def get_examples_preposition(
    preposition, meaning_file="material/meaning_examples.json"
):
    with open(meaning_file) as ex_file:
        example_dict = json.load(ex_file)

    print("Preposition: " + preposition + "\n")

    prep_exists = False
    for meaning, prep_dict in example_dict.items():
        if prep_dict.get(preposition):
            print("[" + meaning + "]")
            for example in prep_dict[preposition]:
                print(example)
            print()
            prep_exists = True

    if not prep_exists:
        print("This preposition does not exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search example sentences for prepositions and/or meanings."
    )

    parser.add_argument("--meaning", "-m", type=str)
    parser.add_argument("--preposition", "-p", type=str)
    parser.add_argument("--file", "-f", type=str)

    args = parser.parse_args()

    # Get only the arguments that are not None.
    arg_list = [arg for arg in vars(args).values() if arg]

    if args.meaning and args.preposition:
        get_example(*arg_list)
    elif args.meaning:
        get_examples_meaning(*arg_list)
    elif args.preposition:
        get_examples_preposition(*arg_list)
    else:
        print("You must either choose a preposition, a meaning or both.")
