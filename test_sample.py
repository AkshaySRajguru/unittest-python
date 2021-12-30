import unittest
from sample import verifyFizzBuzz

class TestSample(unittest.TestCase):
    def testFizz(self):
        for i in [3, 6, 9, 12]:
            self.assertEqual(verifyFizzBuzz(i), 'fizz')
            
    def testBuzz(self):
        for i in [5, 10, 20]:
            self.assertEqual(verifyFizzBuzz(i), 'buzz')
    
    def testFizzBuzz(self):
        for i in [15, 30, 90]:
            self.assertEqual(verifyFizzBuzz(i), 'fizzbuzz')
