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

## Sources

For data collection the following resources have been used.

### Idioms

- https://www.pinterest.com/goranamucic/deutsche-idiome/
- https://www.schreiben.net/artikel/70-redewendungen-bedeutung-herkunft-1635/
- https://de.wikiquote.org/wiki/Deutsche_Sprichw%C3%B6rter
- https://de.wikipedia.org/wiki/Liste_deutscher_Redewendungen