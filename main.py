from functions import introduction_qs, play_again
from decorators import instructions, london_welcome, san_fran_welcome, cairo_welcome, india_welcome
from location_data import Location


def start():
# how to run these sequentially?
    instructions()  # this works in decorators file but not here... ??

    introduction_qs()

    london_welcome()  # this works in decorators file but not here... ??

    London.get_facts()  # help!


    def choose_landmark(dict, list):
        while True:
            choice = input('Where would you like to go? ')
            if choice.upper() == 'NEXT':
                break
            elif int(choice) in dict.keys():
                print('{}: {}'.format(list[int(choice) - 1], dict[int(choice)]))

    def choose_location(list, globe_index):
        while True:
            choice = input('Where would you like to go? ')
            correct_location = globe_index + 1
            if choice == str(list[correct_location]):
                break
            elif choice == globe_index:
                choose_landmark(dict)


    clues = [London_clues, Singapore_clues, San_Fran_clues]

    for location in globe:
        globe_index = globe.index(location)
        for landmark in location:
            print(landmark)
        print('To move to the next location, enter NEXT')
        choose_landmark(clues[globe_index], location)
        for location in location_choices[globe_index]:
            print(location)
        choose_location(correct_route, globe_index)


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