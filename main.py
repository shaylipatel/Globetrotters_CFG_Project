from functions.functions import introduction_qs, winners_graphics_box
from functions.decorators import instructions, london_welcome, san_fran_welcome, cairo_welcome, delhi_welcome, singapore_welcome
from functions.location_data import correct_route
from colorama import Fore, Back, Style


def start():
    # Call the function instructions() to give tell the user how to play.
    instructions()

    # Call the function introduction_qs() to give the user a warm up exercise to make sure they are ready to play!
    introduction_qs()


# Function to choose a landmark in the chosen location
def choose_landmark(location, dict, list):
    print('Enter the landmark number to see if anyone has seen her. \nTo move to the next location, enter NEXT')
    print('\n' + '=' * 145 + '\n')
    while True:  # Will repeat until while loop broken

        try:
            choice = input('Where would you like to go? ').title().strip()
            if choice.upper() == 'NEXT':  # Breaks while loop to go to location list
                break
            elif int(choice) in dict.keys():  # Prints clue for the landmark chosen
                print('{}: {}'.format(list[int(choice) - 1], dict[int(choice)]))
                if location.name == correct_route[4].name and int(choice) == 3:  # Breaks while loop when Ada Lovelace is found
                    break
            else:
                raise Exception
        except:  # Exception raised for invalid choice
            print('\nLandmark not found, please try again! Enter 1, 2 or 3... ')


# Function to choose next location from the location list in the class.
def choose_location(location):
        while True:
            print('=' * 145)
            print('\nWhere would you like to travel to next?')
            for next_location in location.location_list:
                print(next_location)
            print('=' * 145)
            try:
                choice = input('\nWhere would you like to go? ').title()
                if choice.title() == location.correct_location:  # If correct location chosen, while loop breaks
                    break
                elif choice == location.name:  # Option to see clues from previous location (ie. location.landmarks/location.clues)
                    for landmark in location.landmarks:
                        print(Fore.BLACK + Back.WHITE + Style.BRIGHT + landmark)
                        print(Style.RESET_ALL)
                    choose_landmark(location, location.clues, location.landmarks)
                elif choice == location.incorrect_landmark1.name:  # For incorrect location 1, print landmarks and run choose landmark function
                    for landmark in location.incorrect_landmark1.landmarks:
                        print(Fore.BLACK + Back.WHITE + Style.BRIGHT + landmark)
                        print(Style.RESET_ALL)
                    choose_landmark(location, location.incorrect_landmark1.clues,
                                    location.incorrect_landmark1.landmarks)
                elif choice == location.incorrect_landmark2.name:  # For incorrect location 2, print landmarks and run choose landmark function
                    for landmark in location.incorrect_landmark2.landmarks:
                        print(Fore.BLACK + Back.WHITE + Style.BRIGHT + landmark)
                        print(Style.RESET_ALL)
                    choose_landmark(location, location.incorrect_landmark2.clues, location.incorrect_landmark2.landmarks)
                else:
                    raise Exception

            except:
                print('\nInvalid Entry: please try again\n')


# Function to get the correct decorator for the correct location
def choose_decorator(route_index):
        if route_index == 0:  # location.name == 'London':
            london_welcome()
        elif route_index == 1:  # location.name == "Singapore":
            singapore_welcome()
        elif route_index == 2:  # location.name == "San Francisco":
            san_fran_welcome()
        elif route_index == 3:  # location.name == "Delhi":
            delhi_welcome()
        elif route_index == 4:  # location.name == "Cairo":
            cairo_welcome()


# Main body of game
def main_logic():
    for location in correct_route:  # Correct route list imported from location data
        route_index = correct_route.index(location)
        choose_decorator(route_index)
        print('=' * 145 + '\n')
        location.location_facts()  # Prints facts about the chosen location
        print('\n' + '=' * 145 + '\n')
        print('The following landmarks are in {}:'.format(location.name))
        for landmark in location.landmarks:  # Prints landmarks in location.landmarks list
            print(Fore.BLACK + Back.WHITE + Style.BRIGHT + landmark)
            print(Style.RESET_ALL)
        choose_landmark(location, location.clues, location.landmarks)  # Player chooses landmark from list and clues print
        if location.name == correct_route[4].name:  # Breaks for loop once Ada is found in Cairo and move on to final winners_graphics_box() function
            break
        choose_location(location)  # Player chooses where to travel to next


# Run game
start()
main_logic()
winners_graphics_box()