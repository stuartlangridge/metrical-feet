# Word lists by metrical feet

If you're a poet, it's sometimes useful to think about words by their [metrical feet](https://en.wikipedia.org/wiki/Foot_(prosody)); that is, the word POETRY is three syllables, where the first one is stressed and the second two aren't (PO-e-try). So this is a list of lists of words, divided up by their metrical feet (or lexical feet, or lyrics feet, some people call them).

All the hard work is done by the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict); this repository simply contains a list of all the words in that dictionary divided up by their feet, and the simple Python script used to parse `cmudict` into that list.

Files are named after the feet of the words within, so the file containing POETRY will be called 100-something, with 1 meaning "stressed syllable" and 0 meaning "unstressed syllable". Filenames also contain the name of the foot itself in prosody, for four syllables or less; for example, a word which is one unstressed syllable followed by one stressed syllable is 01, and that's named an "iamb" (which is useful if you're writing in iambic pentameter, as Shakespeare often did). Such words (for example ABLAZE, which is ab-LAZE) are thus in a file beginning `01-iamb-`.

The CMU dictionary marks syllables of words as having no stress, primary stress, or secondary stress. Metrical feet don't recognise these two kinds of stress, however, so there are two versions of each word list; one where only primary stress counts as "stressed" and one where both primary and secondary stress count. So `GREEDIER`, for example, which has secondary stress on the first syllable and no stress on the others, is a dactyl (100) if secondary stress counts, and a tribrach (000) if it does not. This means that `GREEDIER` is in files `100-dactyl-include-secondary.txt` and `000-tribrach-primary-only.txt`.

