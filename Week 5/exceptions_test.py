import unittest
from exceptions import valid_user

class TestTryExpect (unittest.TestCase):
    def test_valid(self):
        testcase = "Akshit"
        minlen = 5
        self.assertEqual (valid_user(testcase, minlen), True)

unittest.main()