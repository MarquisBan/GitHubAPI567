import unittest
import HW04a


class APITest(unittest.TestCase):
    def testConnection(self):
        self.assertLessEqual(0, len(HW04a.urlopen('http://github.com').read()))

    def testMBTT(self):
        # Test MarquisBan/TriangleTest
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['TriangleTest'], 7)

    def testMBSS(self):
        # Test MarquisBan/Stevens-SW567
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Stevens-SW567'], 3)

    def testMBSR(self):
        # Test MarquisBan/Student-Repository
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Student-Repository'], 6)


if __name__ == '__main__':
    unittest.main()
