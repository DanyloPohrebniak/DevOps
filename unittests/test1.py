"""Unittests for simple_function from TestClass"""

import unittest
from unittests.app_test_class import TestClass

class TestFile(unittest.TestCase):
    """Tests for simple_function"""
    def test1(self):
        """Test1"""
        tmp = '123'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)

    def test2(self):
        """Test2"""
        tmp = 'Dan'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)

    def test3(self):
        """Test3"""
        tmp = 'Danylo'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)

    def test4(self):
        """Test4"""
        tmp = 'Danylo123'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)

    def test5(self):
        """Test5"""
        tmp = 'DanyloPohrebniak'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
