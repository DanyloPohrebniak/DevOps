"""Unittests for simple_function from TestClass"""

import unittest
from unittests.test_class import TestClass

class TestFile(unittest.TestCase):
    def test1(self):
        tmp = '123'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)


    def test2(self):
        tmp = 'Dan'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)


    def test3(self):
        tmp = 'Danylo'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)

    
    def test4(self):
        tmp = 'Danylo123'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)

    
    def test5(self):
        tmp = 'DanyloPohrebniak'
        result = TestClass.simple_function(tmp)
        self.assertIsNotNone(result)



if __name__ == '__main__':
    unittest.main()