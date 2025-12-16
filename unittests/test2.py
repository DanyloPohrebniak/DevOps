"""Unittests for second_function from TestClass"""

import unittest
from unittests.test_class import TestClass

class TestSecondFunction(unittest.TestCase):
    """Tests for second_function"""

    def test_positive(self):
        """Test1"""
        result = TestClass.second_function(5)
        self.assertEqual(result, "Positive")

    def test_negative(self):
        """Test2"""
        result = TestClass.second_function(-3)
        self.assertEqual(result, "Negative")

    def test_zero(self):
        """Test3"""
        result = TestClass.second_function(0)
        self.assertEqual(result, "Zero")


if __name__ == '__main__':
    unittest.main()
