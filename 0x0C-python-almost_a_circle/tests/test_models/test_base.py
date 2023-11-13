from models.base import Base
import unittest


class TestBase_(unittest.TestCase):
    def test_once(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_noargs(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

if __name__ == "__main__":
    unittest.main()
