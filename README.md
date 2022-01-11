# PPATS
A **PP** **a**ttachment **t**est **s**uite for German

(by [DiveFish](https://github.com/DiveFish/) and [janniss91](https://github.com/janniss91/))

PP attachment is the largest source of errors in syntactic parsing. But what is it exactly that makes it difficult? And which kinds of parsers struggle less with these structures?

The PPATS test suite provides manually created sentences with prepositional phrases that exhibit specific linguistic properties:

|Property | Annotation |
|:------------- |:-------------|
|Base case|`base`|
|1 head candidate|`1head`|
|2 head candidates|All sentences that are not `1head`, `3head`, `4head` or `5head`|
|3 head candidates|`3head`|
|4 head candidates|`4head`|
|5 head candidates|`5head`|
|PP = P + N|`pn`|
|PP = P + D + N|All sentences that are not `pn`, `pdan`, `pppossnp` or `pppp`|
|PP = P + D + A + N|`pdan`|
|Pp = P + D + N + genitive NP|`pppossnp`|
|PP = p + D + N + PP|`pppp`|
|PP before head|`ppfronted`|
|Prepositional object|`objp`|
|Noun-headed PP|`nounheadedpp`|
|PP in idiom|`idm`|

The properties are accessible through the annotations. Parsers can be evaluated against the full test suite or particular properties in order to test their abilities of solving various kinds of PP attachment ambiguities.

The base case consists of a verb-headed PP that has two attachment head candidates which is the most frequent kind of PP attachment ambiguity. The base PP consists of a preposition, a determiner and a noun. This configuration has been selected based on frequencies in the TüBa-D/Z UD corpus (version 11).

## Searching prepositions and meanings

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
These have been obtained from PrepSensNZZ, a licensed corpus of meaning-annotated PPs (Kiss et al. 2016).

To regenerate these statistics, the following must be run:

    python3 tools/number_prep_meaning.py ../prepsensNZZ/ material/prep-meanings/num_prep2meaning.csv material/prep-meanings/top_meanings_per_prep.csv material/prep-meanings/top_preps_per_meaning.csv 

Note: The file names are those that are already present in the repository. For regeneration it might be desirable to change them.

Here is a list of what the 4 arguments to the script must contain:

1. The directory with the files containing the original frequency (PrepSensNZZ) named above.
2. The TSV file that contains a table mapping all prepositions to meanings and stating their combined frequencies.
3. The table that lists the top meanings per preposition (and the overall frequency of the prepositions).
4. The table that lists the top prepositions per meaning (and the overall frequency of the meanings).

## Convert Test Suite to Conll

To convert the test suite to a Conll-X file, use the following command (exchange filenames):

    python3 tools/convert_testsuite_to_conll.py material/pp-test-suite.tsv pp-test-suite.conll


To convert the test suite to a Conll-U file, use the following command (exchange filenames):

    python3 tools/convert_testsuite_to_conll.py material/pp-test-suite.tsv pp-test-suite_u.conll -t u
  
**Note:** The basename of the file must end in "_u" (`filename_u.conll`).

## Convert Conll Formats Between Each Other

To convert a conll-X file to a conll-U file, use the following command:

    python3 tools/change-conll-format.py material/test.conll -u

To convert a conll-U file to a conll-X file, use the following command:

    python3 tools/change-conll-format.py material/test.conll -x

## Sources

For data collection the following resources have been used.

### Idioms

- https://www.pinterest.com/goranamucic/deutsche-idiome/
- https://www.schreiben.net/artikel/70-redewendungen-bedeutung-herkunft-1635/
- https://de.wikiquote.org/wiki/Deutsche_Sprichw%C3%B6rter
- https://de.wikipedia.org/wiki/Liste_deutscher_Redewendungen

## References
PrepSensNZZ: Tibor Kiss, Antje Müller, Claudia Roch, Tobias Stadtfeld, Alicia Katharina Börner and Monika Duzy. 2016. Ein Handbuch für die Bestimmung und Annotation von Präpositionsbedeutungen im Deutschen. Bochum, 1-440. Available here: /media/pages/publikationen/Kiss2016Handbuch/kiss2016handbuch.pdf
