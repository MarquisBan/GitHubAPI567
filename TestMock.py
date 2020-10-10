import HW04a
import unittest
from unittest import mock


def doNothing():
    pass


class TestMockAPI(unittest.TestCase):

    @mock.patch('print', side_effect = doNothing())
    def testAPI(self, mock_test):
        self.assertEqual(HW04a.GitHubAPI('MarquisBan')['StevensSW567'], 3)


if __name__ == '__main__':
    unittest.main()
