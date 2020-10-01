import unittest
import HW04a


class APITest(unittest.TestCase):
    def testConnection(self):
        self.assertLessEqual(0, len(HW04a.urlopen('http://github.com').read()))

    def testRepos(self):
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['TriangleTest'], 7)
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Stevens-SW567'], 3)
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['Student-Repository'], 6)


if __name__ == '__main__':
    unittest.main()
