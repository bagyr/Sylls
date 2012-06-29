import unittest
import logging
import nltk

from haikus import findPattern


class MainSequence(unittest.TestCase):

    def setUp(self):
        self.testString = [
            ('lend me your arms, '
             'fast as thunderbolt, '
             'for a pillow on my journey.')]
        self.testFail = ['When I from black and he from white cloud free']

        self.sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

    def testSimpleHaiku(self):
        self.assertEqual(len(findPattern(self.testString, [17])), 1)
        self.assertEqual(len(findPattern(self.testFail, [17])), 0)
        self.assertEqual(len(findPattern(self.testFail, [3])), 0)
        
    def testComplexHaiku(self):
        self.assertEqual(len(findPattern(self.testString, [5, 5, 7])), 1)
        self.assertEqual(len(findPattern(self.testFail, [5, 5, 7])), 0)
        self.assertEqual(len(findPattern(self.testFail, [5, 5, 7, 10, 14])), 0)

    def testBigFile(self):
        f = open('./conv2.txt')
        text = f.read()
        sent = self.sent_detector.tokenize(text.strip())
        sent = [x.strip() for x in sent[:]]
        simpleHaikus = findPattern(sent, [17])
        complexHaikus1 = findPattern(sent, [5, 7, 5])
        complexHaikus2 = findPattern(sent, [5, 5, 7])
        print 'Big file ', len(simpleHaikus), len(complexHaikus1), len(complexHaikus2)


if __name__ == '__main__':
    unittest.main()
