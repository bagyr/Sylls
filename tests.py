import unittest
import logging
from haikus import findPattern

class MainSequence(unittest.TestCase):

    def setUp(self):
        self.testString = [
            'lend me your arms,\
             fast as thunderbolts, \
             for a pillow on my journey.']
        self.testFail = ['Trolololololo']

    def testSimpleHaiku(self):
        print 'Simple: ', findPattern(self.testString, [17])
        print 'Simple wrong: ', findPattern(self.testFail, [17])
        print 'Simple wrong: ', findPattern(self.testFail, [3])
        
    def testComplexHaiku(self):
        print 'Complex: ', findPattern(self.testString, [5, 7, 5])

if __name__ == '__main__':
    unittest.main()
