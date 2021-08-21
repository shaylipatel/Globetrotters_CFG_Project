import io
import sys
import unittest
from main import start


class TestMain(unittest.TestCase):

    def test_start(self, expected=True):
        # Test the start function

        # Action
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout
        start()  # call function
        # check stdout output

        # Assert
        self.assertTrue(expected, capturedOutput.getvalue())