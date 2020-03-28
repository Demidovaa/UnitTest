# -*- coding: utf-8 -*-
'''
Module for text statistics calculation.
'''

import sys
# from collections import Counter
from collections import defaultdict

def get_char_frequencies(text):
    # result = Counter(text)
    result = defaultdict(int)
    for symbol in text:
        result[symbol] += 1

    return result

def get_unique_words(text):
    result = set(text.split())

    return result

def main():
    print(get_char_frequencies(u"abc"))
    print(get_unique_words(u"Test"))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
