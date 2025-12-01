"""Unittests for second_function from TestClass"""

import unittest
from unittests.test_class import TestClass

class TestSecondFunction(unittest.TestCase):
    """Tests for second_function"""

    def test_positive(self):
        result = TestClass.second_function(5)
        self.assertEqual(result, "positive")

    def test_negative(self):
        result = TestClass.second_function(-3)
        self.assertEqual(result, "negative")

    def test_zero(self):
        result = TestClass.second_function(0)
        self.assertEqual(result, "zero")


if __name__ == '__main__':
    unittest.main()