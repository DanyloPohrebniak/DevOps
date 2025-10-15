import unittest
from temp import simple_function 

class TestFile(unittest.TestCase):
    def test1(self):
        tmp = '123'
        result = simple_function(tmp)
        self.assertIsNotNone(result)


    def test2(self):
        tmp = 'Dan'
        result = simple_function(tmp)
        self.assertIsNotNone(result)


    def test3(self):
        tmp = 'Danylo'
        result = simple_function(tmp)
        self.assertIsNotNone(result)

    
    def test4(self):
        tmp = 'Danylo123'
        result = simple_function(tmp)
        self.assertIsNotNone(result)

    
    def test5(self):
        tmp = 'DanyloPohrebniak'
        result = simple_function(tmp)
        self.assertIsNotNone(result)



if __name__ == '__main__':
    unittest.main()