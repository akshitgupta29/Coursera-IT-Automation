from rearrange import rearrange_name
import unittest as ut

class TestRearrange (ut.TestCase):
    def test_basic (self):
        testcase = "Gupta, Akshit"
        expected = "Akshit Gupta"
        self.assertEqual(rearrange_name(testcase), expected)
    
    #Ths is not considered as a test case since the function doesn't begin with the word test
    def empty_test (self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)

    #This is a valid testcase.
    def test_empty (self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)
ut.main()