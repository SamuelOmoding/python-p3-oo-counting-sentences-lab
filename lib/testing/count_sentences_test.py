#!/usr/bin/env python3

from count_sentences import MyString

import io
import sys

import unittest

# class TestMyString(unittest.TestCase):
#     '''MyString in count_sentences.py'''

#     def test_is_class(self):
#         '''is a class with the name "MyString".'''
#         string = MyString()
#         self.assertIsInstance(string, MyString)

#     def test_value_string(self):
#         '''prints "The value must be a string." if not string.'''
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         string = MyString()
#         string.value = 123
#         sys.stdout = sys.__stdout__
#         self.assertEqual(captured_out.getvalue(), "The value must be a string.\n")

#     def test_is_sentence(self):
#         '''returns True if value ends with a period and False otherwise.'''
#         self.assertTrue(MyString("Hello World.").is_sentence())
#         self.assertFalse(MyString("Hello World").is_sentence())

#     def test_is_question(self):
#         '''returns True if value ends with a question mark and False otherwise.'''
#         self.assertTrue(MyString("Is anybody there?").is_question())
#         self.assertFalse(MyString("Is anybody there").is_question())

#     def test_is_exclamation(self):
#         '''returns True if value ends with an exclamation mark and False otherwise.'''
#         self.assertTrue(MyString("It's me!").is_exclamation())
#         self.assertFalse(MyString("It's me").is_exclamation())

#     def test_count_sentences(self):
#         '''returns the number of sentences in the value.'''
#         simple_string = MyString("one. two. three?")
#         empty_string = MyString()
#         complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
#         self.assertEqual(simple_string.count_sentences(), 3)
#         self.assertEqual(empty_string.count_sentences(), 0)
#         self.assertEqual(complex_string.count_sentences(), 2)

class TestMyString(unittest.TestCase):
    '''MyString in count_sentences.py'''

    def test_is_class(self):
        '''is a class with the name "MyString".'''
        string = MyString()
        self.assertIsInstance(string, MyString)

    def test_value_string(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString()
        string.set_value(123)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "The value must be a string.\n")
        self.assertEqual(string.get_value(), "")

    def test_is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        self.assertTrue(MyString("Hello World.").is_sentence())
        self.assertFalse(MyString("Hello World").is_sentence())

    def test_is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        self.assertTrue(MyString("Is anybody there?").is_question())
        self.assertFalse(MyString("Is anybody there").is_question())

    def test_is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        self.assertTrue(MyString("It's me!").is_exclamation())
        self.assertFalse(MyString("It's me").is_exclamation())

    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
        simple_string = MyString("one. two. three?")
        empty_string = MyString()
        complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
        self.assertEqual(simple_string.count_sentences(), 3)
        self.assertEqual(empty_string.count_sentences(), 0)
        self.assertEqual(complex_string.count_sentences(), 2)

    def test_init_with_non_string_value(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString(123)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "The value must be a string.\n")
        self.assertEqual(string.value, "")