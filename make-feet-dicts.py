#!/usr/bin/env python3

"Parse CMU Pronouncing Dictionary and output dicts of words by metrical foot"

import re, os, glob

FEET = {
    "0": "unstressed",
    "1": "stressed",
    "00": "dibrach",
    "01": "iamb",
    "10": "trochee",
    "11": "spondee",
    "000": "tribrach",
    "001": "anapaest",
    "010": "amphibrach",
    "011": "bacchius",
    "100": "dactyl",
    "101": "cretic",
    "110": "antibacchius",
    "111": "molossus",
    "0000": "tetrabrach",
    "0001": "quartus-paeon",
    "0010": "tertius-paeon",
    "0011": "double-iamb",
    "0100": "secundus-paeon",
    "0101": "diiamb",
    "0110": "antispast",
    "0111": "first-epitrite",
    "1000": "primus-paeon",
    "1001": "choriamb",
    "1010": "ditrochee",
    "1011": "second-epitrite",
    "1100": "double-trochee",
    "1101": "third-epitrite",
    "1110": "fourth-epitrite",
    "1111": "dispondee",
    "x": "unclassified"
}


def get_stress(pron, include_secondary):
    numbers = "".join(re.findall(r"[012]", pron))
    if include_secondary:
        numbers = numbers.replace("2", "1")  # secondary stress treat as primary
    else:
        numbers = numbers.replace("2", "0")  # secondary stress treat as none
    return numbers


def main():
    [os.unlink(x) for x in glob.glob("[0-9]*.txt")]
    byfoot_primaryonly = {}
    byfoot_includesecondary = {}
    with open("cmudict-0.7b", encoding="latin1") as fp:  # http://www.speech.cs.cmu.edu/cgi-bin/cmudict
        defns = [x.strip().split(None, 1) for x in fp.readlines()
                 if not x.startswith(";;;")]
    for word, pron in defns:
        if re.match(r"[0-9]", word): continue
        word = word.replace("_", " ")
        stress_primaryonly = get_stress(pron, include_secondary=False)
        if stress_primaryonly not in byfoot_primaryonly:
            byfoot_primaryonly[stress_primaryonly] = []
        byfoot_primaryonly[stress_primaryonly].append(word)
        stress_includesecondary = get_stress(pron, include_secondary=True)
        if stress_includesecondary not in byfoot_includesecondary:
            byfoot_includesecondary[stress_includesecondary] = []
        byfoot_includesecondary[stress_includesecondary].append(word)

    for stress, words in byfoot_primaryonly.items():
        with open(f"{stress}-{FEET.get(stress, '')}-primary-only.txt", mode="w") as fp:
            fp.write("\n".join(words))
    for stress, words in byfoot_includesecondary.items():
        with open(f"{stress}-{FEET.get(stress, '')}-include-secondary.txt", mode="w") as fp:
            fp.write("\n".join(words))


if __name__ == "__main__":
    main()
