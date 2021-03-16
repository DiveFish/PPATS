# PPATS
A PP attachment test suite for German and Dutch

## Searching Prepositions and Meanings

You can make use of the `search_examples.py` script to search for specific prepositions and meanings. If you specify the filename (optional) it must be in the same JSON format as `meaning_examples.json`.

Use the script in the following way:

Look for example with specific meaning and preposition:

    python3 tools/search_examples.py -m Spatial -p in

Look for all examples for one specific meaning:

    python3 tools/search_examples.py -m Spatial

Look for all examples for one specific preposition:

    python3 tools/search_examples.py -p in

Change the filename (if necessary):

    python3 tools/search_examples.py Spatial -p in -f other_file.json

## Obtaining Preposition-Meaning Frequency Statistics

There are statistics stating the frequencies of prepositions and meanings and their combinations.
These have been obtained from a number of tables (prepsensNZZ) listing this information, which are not included in this repo.

To regenerate these statistics, the following must be run:

    python3 tools/number_prep_meaning.py ../prepsensNZZ/ material/prep-meanings/num_prep2meaning.csv material/prep-meanings/top_meanings_per_prep.csv material/prep-meanings/top_preps_per_meaning.csv 

Note: The file names are those that are already present in the repository. For regeneration it might be desirable to change them.

Here is a list of what the 4 arguments to the script must contain:

1. The directory with the files containing the original frequency (prepsensNZZ) named above.
2. The TSV file that contains a table mapping all prepositions to meanings and stating their combined frequencies.
3. The table that lists the top meanings per preposition (and the overall frequency of the prepositions).
4. The table that lists the top prepositions per meaning (and the overall frequency of the meanings).

## Sources

For data collection the following resources have been used.

### Idioms

- https://www.pinterest.com/goranamucic/deutsche-idiome/
- https://www.schreiben.net/artikel/70-redewendungen-bedeutung-herkunft-1635/
- https://de.wikiquote.org/wiki/Deutsche_Sprichw%C3%B6rter
- https://de.wikipedia.org/wiki/Liste_deutscher_Redewendungen