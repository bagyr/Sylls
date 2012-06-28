import unittest
import logging
from haikus import findPattern

class MainSequence(unittest.TestCase):

    def setUp(self):
        self.testString = ['za cava qawa sadafa gajasa rata paca gata']

    def testSimpleHaiku(self):
        print 'Simple: ', findPattern(self.testString, [18])
        
    def testComplexHaiku(self):
        print 'Complex: ', findPattern(self.testString, [5, 7, 5])

if __name__ == '__main__':
    unittest.main()
