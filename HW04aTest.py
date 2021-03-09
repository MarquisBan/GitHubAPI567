import unittest
import HW04a


class APITest(unittest.TestCase):
    def testConnection(self):
        self.assertLess(0, len(HW04a.urlopen('http://github.com').read()))

    def testMBSS(self):
        # Test MarquisBan/Stevens-SW567 which is not existed
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Stevens-SW567'], 0)

    def testMBSR(self):
        # Test MarquisBan/Student-Repository
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Student-Repository'], 6)


if __name__ == '__main__':
    unittest.main()
