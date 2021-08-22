import io
import sys
import unittest
from functions import affirmation, welcome

class TestStringMethods(unittest.TestCase):
    def test_affirmation(self, expected=True):
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout
        affirmation()  # call function
        # check stdout output
        self.assertTrue(expected, capturedOutput.getvalue())

    def test_welcome(self, expected=True):
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout
        welcome()  # call function
        # check stdout output
        self.assertTrue(expected, capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()