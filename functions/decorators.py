#### INSTRUCTIONS AND WELCOME NOTES USING DECORATORS
from colorama import Fore, Back, Style

# We have used a decorator to emphasise the text that was important - so establishing the instructions and then making it very clear in informing the player of each location that they arrive in.
def text_wrapper(func):
    def inner_wrapper():
        print('\n' + "*" * 145)
        func()
        print("*" * 145 + '\n')
    return inner_wrapper


# Function explaining the instructions to the user.
@text_wrapper
def instructions():
    print('Welcome to the search for Ada Lovelace! Do you think you have what it takes to find one of the most iconic females in computer science…? \nTry and follow the trail of clues she has left behind at famous landmarks to see if you can catch up the world’s first ever computer programmer. \n')
    print('Instructions: \n1. Use the clues to find where Ada travelled to. Determine the correct city and you will be transported there to continue the search. \nChoose the wrong city from the list you will need to try again – and try harder. \nIf you would like to see the 3 clues for your current location again, retype the city name into where you would like to go. \n2. Follow the search from city to city using clues found at famous landmarks. If your intellect matches that of Ada, \nyou may be lucky enough to meet her at the end and gain some wisdom.')
    
    
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
    
    
# welcome = [london_welcome(), singapore_welcome(),san_fran_welcome(), delhi_welcome(), cairo_welcome()]
