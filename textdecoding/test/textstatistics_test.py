# -*- coding: utf-8 -*-
'''
Tests for textstatistics module
'''

import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

import textstatistics


class Test(unittest.TestCase):
    def test_get_char_frequencies_empty(self):
        text = u''
        result = textstatistics.get_char_frequencies(text)
        expected = {}
        self.assertDictEqual(result, expected)

    def test_get_char_frequencies_uniform(self):
        text = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
        result = textstatistics.get_char_frequencies(text)
        expected = {char: 1 for char in text}
        self.assertDictEqual(result, expected)

    def test_get_char_frequencies_simple_text(self):
        text = u'Не слушайте тех, кто говорит дурно о других и хорошо о вас.'
        result = textstatistics.get_char_frequencies(text)
        expected = {
            u'Н': 1,
            u'е': 3,
            u' ': 11,
            u'с': 2,
            u'л': 1,
            u'у': 3,
            u'ш': 2,
            u'а': 2,
            u'й': 1,
            u'т': 4,
            u'х': 3,
            u',': 1,
            u'к': 1,
            u'о': 9,
            u'г': 2,
            u'в': 2,
            u'р': 4,
            u'и': 3,
            u'д': 2,
            u'н': 1,
            u'.': 1,
        }
        self.assertDictEqual(result, expected)

    # New UnitTest

    def test_get_char_frequencies_uniform_char(self):
        text = u'uniform'
        result = textstatistics.get_char_frequencies(text)
        expected = {char: 1 for char in text}
        self.assertDictEqual(result, expected)

    def test_get_char_frequencies_simple_text_test(self):
        text = u'This is not a bug this is a feature'
        result = textstatistics.get_char_frequencies(text)
        expected = {
            u'T': 1,
            u'h': 2,
            u' ': 8,
            u'i': 4,
            u's': 4,
            u'n': 1,
            u'o': 1,
            u't': 3,
            u'a': 3,
            u'b': 1,
            u'u': 2,
            u'g': 1,
            u'f': 1,
            u'e': 2,
            u'r': 1,
        }
        self.assertDictEqual(result, expected)

    # Test for function функции get_unique_words

    def test_get_unique_words(self):
        text = u'This text is a sample text'
        result = textstatistics.get_unique_words(text)
        expected = {'This', 'text', 'is', 'a', 'sample'}
        self.assertEqual(result, expected)

    @unittest.expectedFailure
    def test_get_unique_words_fail(self):
        text = u'This text is a sample text'
        result = textstatistics.get_unique_words(text)
        expected = {'This', 'text'}
        self.assertEqual(result, expected)

    test_text = 'Test'  # test variable

    @unittest.skipIf(test_text != [], "Сheck")
    def test_get_unique_words_skip(self):
        text = u'This text is a sample text'
        result = textstatistics.get_unique_words(text)
        expected = {'This', 'text', 'is', 'a', 'sample'}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
