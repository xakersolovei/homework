#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""


from pathlib import Path
import string
from collections import Counter

f = Path(__file__).parent.absolute() / "king_james_bible.txt"
BIBLE = f.read_text()


def most_freq_bible_words(n: int) -> list:
    bible = BIBLE.split()
    list = []

    for word in bible:
        for znak in string.punctuation:
            word = word.replace(znak, '')
        list.append(word.lower())

    super_slova = Counter(list).most_common(n)

    return [i[0] for i in super_slova]


if __name__ == "__main__":
    print(*most_freq_bible_words(10), sep="\n")
