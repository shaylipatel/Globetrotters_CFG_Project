import io
import sys
import unittest
from functions import play_again
# this does not work
# need to work on this !!!!

class TestStringMethods(unittest.TestCase):
    def test_play_again(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        play_again()                                    # Call function.
        self.assertEqual(capturedOutput.getvalue(), "The game will play again.\n") #check stdout output

# print statements used to find issue
if __name__ == '__main__':
    print('3')
    # code stops running here ??
    # need to try and fix this
    unittest.main()
    print('4')

print('hello')
