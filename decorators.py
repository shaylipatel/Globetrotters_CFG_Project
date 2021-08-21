#### INSTRUCTIONS AND WELCOME NOTES USING DECORATORS
from colorama import Fore, Back, Style
# We have used a decorator to emphasise the text that was important - so establishing the instructions and then making it very clear in informing the player of each location that they arrive in.

def text_wrapper(func):
    def inner_wrapper():
        print("*" * 120)
        func()
        print("*" * 120)
    return inner_wrapper


# Function explaining the instructions to the user.
@text_wrapper
def instructions():
    print('Welcome to the search for Ada Lovelace. With her vast knowledge of mathematics and her vision of what was possible \nfor the future of machines, she is today known as the first programmer. However Ada has been travelling around the \nworld for many years, from country to country. As a young budding programmer, your job is to find Ada, and see what \nknowledge and wisdom she is willing to impart to you.\n \nDo you think you have what it takes to find the elusive Ada…? \nFollow the trail of clues she has left behind to see if you can outwit the world’s first ever computer programmer. \n')
    print('Instructions: \n1. You will start in London. Use the clues to resolve where Ada travelled to next. Pick the correct city and you \nwill be transported there to continue the search. Pick the wrong city and you will return to London to try again \n– and try harder. \n2. Follow the search from city to city. If your intellect matches that of Ada, you may be lucky enough to meet her \nat the end and win the game.')

    
# Function for when the user enters London.  
@text_wrapper
def london_welcome():
    print(Fore.BLACK + Back.WHITE + Style.BRIGHT + 'Welcome to sunny London! \n…where the sun shines in between the bursts of rain! Follow the clues to figure out which city Ada went to next.')
    print(Style.RESET_ALL)
    
# Function for when the user enters Singapore.
@text_wrapper
def singapore_welcome():
    print(Fore.BLACK + Back.WHITE + Style.BRIGHT + 'Welcome to Singapore! \nThe city where summer resides all year long with breathtaking skyline views at night of buildings lit to the nines!')
    print(Style.RESET_ALL)
    
# Function for when the user enters San Francisco.
@text_wrapper
def san_fran_welcome():
    print(Fore.BLACK + Back.WHITE + Style.BRIGHT + 'Welcome to San Francisco! The city of the golden gate! The home of Silicon Valley! \nWhat gold will you find here and where will this currency take you next?')
    print(Style.RESET_ALL)
    
# Function for when the user enters Cairo.
@text_wrapper
def cairo_welcome():
    print(Fore.BLACK + Back.WHITE + Style.BRIGHT + 'Welcome to the delightful city of Cairo! Careful - Don’t lose your sun hat in the hustle and bustle! \nLet’s see what wisdoms and secrets this ancient city of the Pharaohs is willing to impart with you. \nAnd whether it will give you a treasure or a curse.')
    print(Style.RESET_ALL)
    
# Function for when the user enters Delhi.
@text_wrapper
def delhi_welcome():
    print(Fore.BLACK + Back.WHITE + Style.BRIGHT + 'Welcome to Delhi! \nThe street markets are lively, the colours vibrant and the food incredible. \nJust watch out for that Dehli Belly… it can’t get in the way of your mission!')
    print(Style.RESET_ALL)    

    
if __name__ == '__main__': 
    instructions()
    london_welcome()
    san_fran_welcome()
    cairo_welcome()
    delhi_welcome()
    
    
#welcome = [london_welcome(), singapore_welcome(),san_fran_welcome(), delhi_welcome(), cairo_welcome()]
