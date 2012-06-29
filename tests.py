import unittest
import logging
from haikus import findPattern

class MainSequence(unittest.TestCase):

    def setUp(self):
        self.testString = [
            ('lend me your arms, '
             'fast as thunderbolt, '
             'for a pillow on my journey.')]
        self.testFail = ['When I from black and he from white cloud free']

    def testSimpleHaiku(self):
        print 'Simple: ', findPattern(self.testString, [17])
        print 'Simple wrong: ', findPattern(self.testFail, [17])
        print 'Simple wrong: ', findPattern(self.testFail, [3])
        
    def testComplexHaiku(self):
        print 'Complex: ', findPattern(self.testString, [5, 5, 7])

if __name__ == '__main__':
    unittest.main()
