#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle

""" Define class test """


class testsquare(unittest.TestCase):
    """ These are tests for the square class """
    def test_if_inherits(self):
        """Tests if class inherites from another"""
        self.assertTrue(issubclass(Square, Rectangle))

