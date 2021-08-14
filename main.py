from functions import introduction_qs, play_again
from decorators import instructions, london_welcome, san_fran_welcome, cairo_welcome, india_welcome
from location_data import correct_route


def start():
##how to run these sequentially?
    instructions()  # this works in decorators file but not here... ??

    introduction_qs()

    london_welcome()  # this works in decorators file but not here... ??

    correct_route[0].location_facts()  # i changed get_facts() to location_facts() and it works now

def main_logic():
    def choose_landmark(dict, list):
        while True:
            choice = input('Where would you like to go? ')
            if choice.upper() == 'NEXT':
                break
            elif int(choice) in dict.keys():
                print('{}: {}'.format(list[int(choice) - 1], dict[int(choice)]))

    def choose_location(location):
        while True:
            for next_location in location.location_list:
                print(next_location)
            choice = input('Where would you like to go? ')
            if choice == location.correct_location:
                break
            elif choice == location.incorrect_landmark1.name:
                incorrect_landmark = location.incorrect_landmark1
            elif choice == location.incorrect_landmark2.name:
                incorrect_landmark = location.incorrect_landmark2
            if incorrect_landmark == location.incorrect_landmark1 or incorrect_landmark ==location.incorrect_landmark2:
                for landmark in incorrect_landmark.landmarks:
                    print (landmark)

                choose_landmark(location.incorrect_landmark1.clues, location.incorrect_landmark1.landmarks)


    for location in correct_route:
        route_index = correct_route.index(location)
        for landmark in location.landmarks:
            print(landmark)
        print('To move to the next location, enter NEXT')
        choose_landmark(location.clues, location.landmarks)
        choose_location(location)


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
# start()

main_logic()
