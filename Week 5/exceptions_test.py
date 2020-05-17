import unittest
from exceptions import valid_user

class TestTryExpect (unittest.TestCase):
    def test_valid(self):
        testcase = "Akshit"
        minlen = 5
        self.assertEqual (valid_user(testcase, minlen), True)

    def test_too_short (self):
        testcase = "Ak"
        minlen = 5
        self.assertEqual(valid_user(testcase, minlen), False)
    
    def test_invalid_character (self):
        testcase = "Akshit_Gupta"
        minlen = 5
        self.assertEqual(valid_user(testcase, minlen), False)

    def test_invalid_len (self):
        testcase = "Akshit"
        minlen = -1
        self.assertRaise

unittest.main()