import io
import sys
import unittest
from functions import affirmation, welcome

class TestStringMethods(unittest.TestCase):
    
    def test_affirmation(self, expected=True):
        # Test the affirmation function
        
        # Action
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput  # Rredirect stdout
        affirmation()  # Call function
        # Check stdout output
        
        # Assert
        self.assertTrue(expected, capturedOutput.getvalue())

    def test_welcome(self, expected=True):
        # Test the welcome function
        
        # Action
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput  # Redirect stdout
        welcome()  # Call function
        # Check stdout output
        
        # Assert
        self.assertTrue(expected, capturedOutput.getvalue())

        
if __name__ == '__main__':
    unittest.main()
