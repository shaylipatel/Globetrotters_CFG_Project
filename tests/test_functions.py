import io
import sys
import unittest
from functions import play_again, introduction_qs


class TestStringMethods(unittest.TestCase):

    def test_play_again(self, expected=True):
        # Test the play_again function

        # Action
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout
        play_again()  # call function
        # check stdout output

        # Assert
        self.assertTrue(expected, capturedOutput.getvalue())

    def test_introduction_qs(self, expected=True):
        # Test the introduction_qs function

        # Action
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout
        introduction_qs()  # call function
        # check stdout output

        # Assert
        self.assertTrue(expected, capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()


