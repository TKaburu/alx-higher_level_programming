#!/usr/bin/python3

""" import modules """

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


""" Define test class """


class TestSquare(unittest.TestCase):
    def test_inheritance(self):
        """ Checks if class inherits from another """
        self.assertTrue(issubclass(Square, Rectangle))
