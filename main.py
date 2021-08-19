from functions import introduction_qs
from decorators import instructions, london_welcome, san_fran_welcome, cairo_welcome, delhi_welcome, singapore_welcome
from location_data import correct_route
# import time


def start():
    instructions()  # Call the function instructions() to give tell the user how to play.

    introduction_qs()  # Call the function introduction_qs() to give the user a warm up exercise to make sure they are ready to play!

def main_logic():
    def choose_landmark(dict, list):
        while True:
            try:
                choice = input('Where would you like to go? ').title()
                if choice.upper() == 'NEXT':
                    break

                elif int(choice) in dict.keys():
                    print('{}: {}'.format(list[int(choice) - 1], dict[int(choice)]))
                else:
                    raise AttributeError
            except AttributeError:
                print('Invalid landmark, please try again!')

    def choose_location(location):
        while True:
            for next_location in location.location_list:
                print(next_location)
            try:
                choice = input('Where would you like to go? ').title()

                if choice.title() == location.correct_location:
                    break
                elif choice == location.incorrect_landmark1.name:
                    incorrect_landmark = location.incorrect_landmark1
                elif choice == location.incorrect_landmark2.name:
                    incorrect_landmark = location.incorrect_landmark2
                else:
                    raise AttributeError
                if incorrect_landmark == location.incorrect_landmark1 or incorrect_landmark == location.incorrect_landmark2:
                    for landmark in incorrect_landmark.landmarks:
                        print(landmark)
                    print('Enter the landmark number to see if anyone has seen her. \nTo move to the next location, enter NEXT')
                    choose_landmark(location.incorrect_landmark1.clues, location.incorrect_landmark1.landmarks)
            except AttributeError: # exception handling exits game to mitigate Attribute Error in location list and clues ending at Cairo
                print('INVALID ENTRY: please try again')
                    # print('GAME OVER!')
                    # exit() # without exit statement , creates an infinite loop.
    def choose_wrapper(location):
        if route_index == 0: #location.name == 'London':
            london_welcome()
        elif route_index == 1: #location.name == "Singapore":
            singapore_welcome()
        elif route_index == 2: #location.name == "San Francisco":
            san_fran_welcome()
        elif route_index == 3: #location.name == "Delhi":
            delhi_welcome()
        elif route_index == 4: #location.name == "Cairo":
            cairo_welcome()

    for location in correct_route:
        route_index = correct_route.index(location)
        choose_wrapper(location)
        print('=' * 120)
        print(location.location_facts())
        print('=' * 120)
        print('The following landmarks are in {}:'.format(location.name))
        for landmark in location.landmarks:
            print(landmark)
        print('Enter the landmark number to see if anyone has seen her. \nTo move to the next location, enter NEXT')
        choose_landmark(location.clues, location.landmarks)
        print('Where would you like to travel to next?')
        choose_location(location)

start()
main_logic()



    #     # more text to describe the situation ??
    #     print("You see three people. You decide to approach one of them in hopes to track down [ enter name ].")
    #
    #     print('What state in the United States will you fly out to?')
    #     # convert the player's input() to lower_case
    #     answer = input(">").lower()
    #
    #     if answer == 'california':
    #         california_welcome()
    #         California()
    #     else:
    #         print('You decide to fly to', answer, '.')
    #         print(
    #             'Once you arrive there and come off the plane you notice [ enter something ]. You realise you are in the wrong place. You swiftly return to London to look for more clues.')
    #
    #
    # start the game

