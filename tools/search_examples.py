import argparse
import json


def get_example(meaning, preposition, meaning_file="material/meaning_examples.json"):
    with open(meaning_file) as ex_file:
        example_dict = json.load(ex_file)
        print("meaning\tpreposition\texample")

        if example_dict.get(meaning):
            if example_dict[meaning].get(preposition):
                for example in example_dict[meaning][preposition]:
                    print(meaning + "\t" + preposition + "\t" + example)
            else:
                print("The preposition does not have this meaning or does not exist.")
        else:
            print("This meaning does not exist.")


def get_examples_meaning(meaning, meaning_file="material/meaning_examples.json"):
    with open(meaning_file) as ex_file:
        example_dict = json.load(ex_file)

    print("meaning\tpreposition\texample")

    if example_dict.get(meaning):
        for prep, example_list in example_dict[meaning].items():
            for example in example_list:
                print(meaning + "\t" + prep + "\t" + example)
    else:
        print("This meaning does not exist.")


def get_examples_preposition(
    preposition, meaning_file="material/meaning_examples.json"
):
    with open(meaning_file) as ex_file:
        example_dict = json.load(ex_file)

    print("meaning\tpreposition\texample")

    prep_exists = False
    for meaning, prep_dict in example_dict.items():
        if prep_dict.get(preposition):
            for example in prep_dict[preposition]:
                print(meaning + "\t" + preposition + "\t" + example)
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
