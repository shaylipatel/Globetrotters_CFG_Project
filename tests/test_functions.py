import io
import sys
import unittest
from functions import play_again

class TestStringMethods(unittest.TestCase):
    def test_play_again(self, expected=True):
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout
        play_again()  # call function
        # check stdout output
        self.assertTrue(expected, capturedOutput.getvalue())

# print statements used to find issue
if __name__ == '__main__':
    print('3')
    # code stops running here ??
    # need to try and fix this
    unittest.main()
    print('4')

print('hello')
