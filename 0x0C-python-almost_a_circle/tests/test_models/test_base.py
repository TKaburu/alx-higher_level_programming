#!/usr/bin/python3

""" import modules """

from models.base import Base
import unittest


""" define test class """


class TestBase_(unittest.TestCase):
    def test_once(self):
        """checks if the test runs once"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_noargs(self):
        """Tests for no arguments """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

if __name__ == "__main__":
    unittest.main()
