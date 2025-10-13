import csv
from pathlib import Path
from typing import List, Dict


def read_feature_tsv(tsv_path: str) -> Dict[str, Dict[str, str]]:
    """
    Reads the TSV and returns a mapping from sentence string to a dict of feature values.
    """
    sentence_to_features = {}
    with open(tsv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            sentence = row["sentence"].strip()
            distance = int(row["head_distance"])

            # Binning
            if 0 < distance <= 4:
                dist_bin = "dist_0_4"
            elif 4 < distance <= 8:
                dist_bin = "dist_4_8"
            elif 8 < distance <= 12:
                dist_bin = "dist_8_12"
            else:
                dist_bin = "dist_other"

            sentence_to_features[sentence] = {
                "distance": dist_bin,
                "prep-pos": int(row["prep_position"]) + 1,
                "prepobj-pos": int(row["prep_obj_position"]) + 1,
            }

    return sentence_to_features


def read_conll_file(path: str) -> List[List[List[str]]]:
    """
    Reads a CoNLL file and returns a list of sentences, each sentence is a list of token columns.
    """
    with open(path, encoding="utf-8") as f:
        content = f.read().strip()

    sentences = []
    for sent_block in content.split("\n\n"):
        tokens = [line.split("\t") for line in sent_block.split("\n") if line.strip()]
        if tokens:
            sentences.append(tokens)
    return sentences


def write_conll_file(path: str, sentences: List[List[List[str]]]) -> None:
    """
    Writes modified CoNLL data back to file.
    """
    with open(path, "w", encoding="utf-8") as f:
        for sentence in sentences:
            for token in sentence:
                f.write("\t".join(token) + "\n")
            f.write("\n")


def sentence_to_str(tokens: List[List[str]]) -> str:
    """
    Converts list of token lines into a single sentence string.
    """
    return " ".join(token[1] for token in tokens)


def add_features_to_props(conll_dir: str, tsv_path: str, output_dir: str) -> None:
    """
    Modifies all .conll files in a directory by injecting features from the TSV,
    and writes the modified files to a separate output directory.
    """
    feature_data = read_feature_tsv(tsv_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for conll_file in Path(conll_dir).glob("*.conll"):
        print(f"Processing: {conll_file}")
        sentences = read_conll_file(str(conll_file))
        updated_sentences = []

        for tokens in sentences:
            sentence_str = sentence_to_str(tokens)
            features = feature_data.get(sentence_str)

            if features:
                for token in tokens:
                    # props are in 6th column (index 5)
                    old_props = token[5] if token[5] != "_" else ""
                    full_props = old_props.split("|") if old_props else []
                    new_props = [f"{key}:{val}" for key, val in features.items()]
                    full_props.extend(new_props)
                    token[5] = "|".join(full_props)
            updated_sentences.append(tokens)

        output_file = output_path / conll_file.name
        write_conll_file(str(output_file), updated_sentences)

        print(f"✅ Written: {output_file}\n")


if __name__ == "__main__":
    TSV_FEATURE_FILE = "/Users/patricia/Code/PPATS/material/pp-test-suite.tsv"
    CONLL_INPUT_DIR = "/Users/patricia/Code/PPATS/material"
    CONLL_OUTPUT_DIR = "/Users/patricia/Code/PPATS/material/with_tsv_props"

    add_features_to_props(CONLL_INPUT_DIR, TSV_FEATURE_FILE, CONLL_OUTPUT_DIR)
