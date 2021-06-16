import csv
import sys


def read_annotated_conll():
    with open("material/pp-test-suite-annotated.conll") as annotated:
        reader = csv.reader(annotated, delimiter="\t")

        categories = {}
        sentences = {}
        sentence = []
        current_sentence = 1
        current_cat = None
        for token_line in reader:
            # Define the current sentence category.
            if token_line:
                features = token_line[5]
                props = features.split("|")[-2]
                cat = props.split(":")[-1]

                if cat != current_cat and current_cat is not None:
                    categories[current_cat] = sentences
                    current_sentence = 1
                    sentences = {}
                
                current_cat = cat
                sentence.append(token_line)
            else:
                sentences[current_sentence] = sentence
                current_sentence += 1
                # Re-initialize Sentence List.
                sentence = []
                
        return categories


def test_sent_num_per_category(categories):
    for cat, sentences in categories.items():
        assert len(sentences) == 15


def test_equality(categories):
    for cat, sentences in categories.items():
        sentences = list(sentences.values())
        # Use the first sentence as benchmark for comparison.
        first_sentence = sentences[0]
        for token_num, token in enumerate(first_sentence):
            _, _, lemma, upos, xpos, features = token
            _, _, _, tf = features.split("|")

            for sent_num, sentence in enumerate(sentences[1:], start=2):
                try:
                    _, _, lemma2, upos2, xpos2, features2 = sentence[token_num]
                    _, _, _, tf2 = features2.split("|")
                except IndexError:
                    print("Wrong length of sentence '{}' in category '{}'\n".format(sent_num, cat))
                    continue
                try:
                    assert upos == upos2
                except AssertionError:
                    print("'{}' is not '{}' in token '{}' in sentence '{}' in category '{}'".format(upos, upos2, sentence[token_num], sent_num, cat))
                    stop = input("Press enter to go to next example / stop to exit program: ")
                    print()
                    if stop == "stop":
                        sys.exit()

                try:
                    assert xpos == xpos2
                except AssertionError:
                    print("'{}' is not '{}' in token '{}' in sentence '{}' in category '{}'".format(xpos, xpos2, sentence[token_num], sent_num, cat))
                    stop = input("Press enter to go to next example / stop to exit program: ")
                    print()
                    if stop == "stop":
                        sys.exit()
                try:   
                    assert tf == tf2
                except AssertionError:
                    print("'{}' is not '{}' in token '{}' in sentence '{}' in category '{}'".format(tf, tf2, sentence[token_num], sent_num, cat))
                    stop = input("Press enter to go to next example / stop to exit program.: ")
                    print()
                    if stop == "stop":
                        sys.exit()


if __name__ == "__main__":

    categories = read_annotated_conll()

    # Run assertions in test functions.
    test_sent_num_per_category(categories)
    test_equality(categories)
