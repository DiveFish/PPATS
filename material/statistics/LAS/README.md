# Filtered LAS for PPs

## General remarks
For prepositions, preposition-noun and preposition-order combinations, a minimum frequency of 10 was required to be listed in the statistics. If more than 20 items reached this threshold, only the 20 items with the lowest LAS were included. Attachment scores represent results from the `dpar` baseline parser compared to the gold standard.

## Content
* `prep-nmod`: LAS for all prepositions where the PP is in an nmod relation to the (nominal) head
* `prep-noun-nmod`: LAS for all combinations of preposition+noun (the components of a PP) where the PP is in an nmod relation to the (nominal) head
* `prep-noun-obl`: LAS for all combinations of preposition+noun (the components of a PP) where the PP is in an obl relation to the (verbal) head
* `prep-obl`: LAS for all prepositions where the PP is in an obl relation to the (verbal) head
* `prep-ord-nmod`: LAS for all prepositions preceding or following the nominal head of the PP via the nmod relation
* `prep-ord-obl`: LAS for all prepositions preceding or following the verbal head of the PP via the obl relation
