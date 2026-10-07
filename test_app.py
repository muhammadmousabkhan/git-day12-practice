import unittest

from app import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 10)

    def test_add_zero(self):
        self.assertEqual(add(5, 3), 10)


if __name__ == "__main__":
    unittest.main()