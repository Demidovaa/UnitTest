# -*- coding: utf-8 -*-
'''
Module for text statistics calculation.
'''

import sys
from collections import Counter

def get_char_frequencies(text):
    result = Counter(text)
    return result

def main():
    print(get_char_frequencies(u"abc"))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
