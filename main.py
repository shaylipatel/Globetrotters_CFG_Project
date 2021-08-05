from functions import introduction_qs, play_again
from decorators import instructions, london_welcome, california_welcome

def California():
    print("\nYou have arrived in California!") # could have california_welcome() function in place of this line
    print("You see three people and decide to approach one of them in hopes to find a clue. Who do you approach")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.")

    # take input()
    answer = input(">")

    if answer == "1":
        print('option 1')
    elif answer == "2":
        print('option 2')
    else:
        print('this is not an option.')


def start():

    instructions()
    
    introduction_qs()

    name = str(input('Please input your name: Agent '))
    print("'Hello Agent", name.title(), "you have been selected for a secret mission.'")

    # write the information about the game here [instructions for the user]
    # use decorators
    # following the bad guy, must used hints to follow them and track them down ?? >> why ?? justice idk

    london_welcome()
    #print("You are currently in London, UK.")

    # more text to describe the situation ??
    print("You see three people. You decide to approach one of them in hopes to track down [ enter name ].")

    print('What state in the United States will you fly out to?')
    # convert the player's input() to lower_case
    answer = input(">").lower()

    if answer == 'california':
        california_welcome()
        California()
    else:
        print('You decide to fly to', answer, '.')
        print(
            'Once you arrive there and come off the plane you notice [ enter something ]. You realise you are in the wrong place. You swiftly return to London to look for more clues.')








# start the game
start()
