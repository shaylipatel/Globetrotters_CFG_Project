import unittest
from decorators import instructions, instructions1


class TestIntro(unittest.TestCase):
    # this only works if i define the instructions() function without calling the decorator
    def test_instructions1(self):
        # Test the instructions function
        
        # Assume
        x = 'Welcome to the hunt for Ada Lovelace! Do you think you have what it takes to find the elusive Ada…? \nFollow the trail of clues she has left behind to see if you can outwit the world’s first ever computer programmer. \n'
        y = 'Instructions: \n1. You will start in London. Use the clues to resolve where Ada travelled to next. Pick the correct city and you \nwill be transported there to continue the search. Pick the wrong city and you will return to London to try again \n– and try harder. \n2. Follow the search from city to city. If your intellect matches that of Ada, you may be lucky enough to meet her \nat the end and win the game.'
        expected = x + y
        # Action
        result = instructions1()
        # Assert
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
