import io
import sys
import unittest
from decorators import instructions, london_welcome, san_fran_welcome, singapore_welcome, delhi_welcome, cairo_welcome


class TestIntro(unittest.TestCase):

    def test_instructions(self):
        # Test the instructions function
        
        # Assume
        d = '************************************************************************************************************************'
        x = 'Welcome to the hunt for Ada Lovelace! Do you think you have what it takes to find the elusive Ada…? \nFollow the trail of clues she has left behind to see if you can outwit the world’s first ever computer programmer. \n'
        y = '\nInstructions: \n1. You will start in London. Use the clues to resolve where Ada travelled to next. Pick the correct city and you \nwill be transported there to continue the search. Pick the wrong city and you will return to London to try again \n– and try harder. \n2. Follow the search from city to city. If your intellect matches that of Ada, you may be lucky enough to meet her \nat the end and win the game.\n'
        d = '************************************************************************************************************************\n'
        expected = d + x + y + d

        # Action
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # Redirect stdout.
        instructions()

        # Assert
        self.assertEqual(expected, capturedOutput.getvalue())

    def test_londone_welcome(self):
        # Test the london_welcome function

        # Assume
        d = '************************************************************************************************************************'
        x = 'Welcome to sunny London! \n…where the sun shines in between the bursts of rain! Follow the clues to figure out which city Ada went to next.\n'
        d = '************************************************************************************************************************\n'
        expected = d + x + d

        # Action
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # Redirect stdout.
        london_welcome()

        # Assert
        self.assertEqual(expected, capturedOutput.getvalue())

    def test_san_fran_welcome(self):
        # Test the san_fran_welcome function

        # Assume
        d = '************************************************************************************************************************'
        x = 'Welcome to San Francisco! The city of the golden gate! The home of Silicon Valley! \nWhat gold will you find here and where will this currency take you next?\n'
        d = '************************************************************************************************************************\n'
        expected = d + x + d

        # Action
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # Redirect stdout.
        san_fran_welcome()

        # Assert
        self.assertEqual(expected, capturedOutput.getvalue())

    def test_singapore_welcome(self):
        # Test the singapore_welcome function

        # Assume
        d = '************************************************************************************************************************'
        x = 'Welcome to Singapore! \nThe city where summer resides all year long with breathtaking skyline views at night of buildings lit to the nines!\n'
        d = '************************************************************************************************************************\n'
        expected = d + x + d

        # Action
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # Redirect stdout.
        singapore_welcome()

        # Assert
        self.assertEqual(expected, capturedOutput.getvalue())

    def test_delhi_welcome(self):
        # Test the delhi_welcome function

        # Assume
        d = '************************************************************************************************************************'
        x = 'Welcome to Delhi! \nThe street markets are lively, the colours vibrant and the food incredible. \nJust watch out for that Dehli Belly… it can’t get in the way of your mission!\n'
        d = '************************************************************************************************************************\n'
        expected = d + x + d

        # Action
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # Redirect stdout.
        delhi_welcome()

        # Assert
        self.assertEqual(expected, capturedOutput.getvalue())

    def test_cairo_welcome(self):
        # Test the cairo_welcome function

        # Assume
        d = '************************************************************************************************************************'
        x = 'Welcome to the delightful city of Cairo!  Careful - Don’t lose your sun hat in the hustle and bustle! \nLet’s see what wisdoms and secrets this ancient city of the Pharaohs is willing to impart with you. \nAnd whether it will give you a treasure or a curse.\n'
        d = '************************************************************************************************************************\n'
        expected = d + x + d

        # Action
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # Redirect stdout.
        cairo_welcome()

        # Assert
        self.assertEqual(expected, capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()
