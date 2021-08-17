from functions import introduction_qs
from decorators import instructions, london_welcome, san_fran_welcome, cairo_welcome, india_welcome, singapore_welcome
from location_data import correct_route
import time


def start():
   
   instructions()  # Call the function instructions() to give tell the user how to play.
   
   introduction_qs()  # Call the function introduction_qs() to give the user a warm up exercise to make sure they are ready to play!

   london_welcome() # Call the function london_welcome(), it welcomes the user to the first location... London!
   print('=' * 120)
   correct_route[0].location_facts() # Displays facts about London to the user.
   correct_route[0].get_weather()
   print('=' * 120)


   def main_logic():
      def choose_landmark(dict, list):
         while True:
            choice = input('Where would you like to go? ').title()
            if choice.upper() == 'NEXT':
                break
            elif int(choice) in dict.keys():
                print('{}: {}'.format(list[int(choice) - 1], dict[int(choice)]))
                break
            # add some exception handling here
                  

      def choose_location(location):
        while True:
            for next_location in location.location_list:
                print(next_location)
            choice = input('Where would you like to go? ').title()
            if choice.title() == location.correct_location:
                # Location == Singapore
                if choice.title() == 'Singapore':
                    singapore_welcome()
                    print('=' * 120)
                    correct_route[1].location_facts()
                    correct_route[1].get_weather()
                    print('=' * 120)
                    break

                # Location == San Francisco
                if choice.title() == 'San Francisco':
                    san_fran_welcome()
                    print('=' * 120)
                    correct_route[2].location_facts()
                    correct_route[2].get_weather()
                    print('=' * 120)
                    break

                # Location == Cairo
                if choice.title() == 'Cairo':
                    cairo_welcome()
                    print('=' * 120)
                    correct_route[4].location_facts()
                    correct_route[4].get_weather()
                    print('=' * 120)
                    break

                # Location == Delhi
                if choice.title() == 'Delhi':
                    india_welcome()
                    print('=' * 120)
                    correct_route[3].location_facts()
                    correct_route[3].get_weather()
                    print('=' * 120)
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


   main_logic()
start()


