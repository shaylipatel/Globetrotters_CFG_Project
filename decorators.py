#### INSTRUCTIONS AND WELCOME NOTES USING DECORATORS

# why does it say none when you print the functions??

def text_wrapper(func):
    def inner_wrapper():
        print("*" * 120)
        func()
        print("*" * 120)
    return inner_wrapper


@text_wrapper
def instructions():
    print('Welcome to the hunt for Ada Lovelace! Do you think you have what it takes to find the elusive Ada…? \nFollow the trail of clues she has left behind to see if you can outwit the world’s first ever computer programmer. \n')
    print('Instructions: \n1. You will start in London. Use the clues to resolve where Ada travelled to next. Pick the correct city and you \nwill be transported there to continue the search. Pick the wrong city and you will return to London to try again \n– and try harder. \n2. Follow the search from city to city. If your intellect matches that of Ada, you may be lucky enough to meet her \nat the end and win the game.')

print(instructions())


@text_wrapper
def london_welcome():
    print('Welcome to sunny London! \n…where the sun shines in between the bursts of rain! Follow the clues to figure out which city Ada went to next.')

print(london_welcome())


@text_wrapper
def california_welcome():
    print('Welcome to California! The golden state! The land of beaches! \nWhat gold (or sand) will you find here and where will this currency take you next?')

print(california_welcome())


@text_wrapper
def cairo_welcome():
    print('Welcome to the delightful city of Cairo!  Careful - Don’t lose your sun hat in the hustle and bustle! \nLet’s see what wisdoms and secrets this ancient city of the Pharaohs is willing to impart with you. \nAnd whether it will give you a treasure or a curse.')

print(cairo_welcome())


@text_wrapper
def india_welcome():
    print('Welcome to Delhi! \nThe street markets are lively, the colours vibrant and the food incredible. \nJust watch out for that Dehli Belly… it can’t get in the way of your mission!')

print(india_welcome())





