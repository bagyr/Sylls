import unittest
from haikus import findPattern


class MainSequence(unittest.TestCase):

    def setUp(self):
        pass

    def testFind(self):
        testString = ['za cava qawa sadafa gajasa rata paca gata']
        found1 = findPattern(testString, [17])
        found2 = findPattern(testString, [5, 7, 5])
        print found1, found2

if __name__ == '__main__':
    unittest.main()
