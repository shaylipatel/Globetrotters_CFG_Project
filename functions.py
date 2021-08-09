from main import start

# function to asks the user if they want to play again
def play_again():
    print("\nDo you want to play again? (y or n)")

    # convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        print('okay')

  
# a bit of fun at the beginning to get the game going, and add in more steps, extending it:
def introduction_qs():
    answer = input("The first item required for this game of wits is COURAGE. \nDo you have a heart of solid gold and are you ready to take on the search for Ada Lovelace? (yes/no) ")
    if answer.lower().strip() == 'yes':
        answer = input(("Excellent! A half-worthy candidate. \nThe second item required for this mission is an INTELLECT as sharp as the Kohinoor diamond. Is this something you possess young Philosopher? (yes/no) "))
        if answer.lower().strip() == 'yes':
            answer = input("The first thing to determine is where the trail starts... \nWhere would the world's first computer programmer start her jounrey... and so where should you? London, New York or Paris? \n")
            if answer.lower().strip() == 'london':
                print("Excellent choice! Proceed to London and begin the searching process... the clues are waiting... no dilly-dally-ing.")
            elif answer.lower().strip() == 'new york':
                print("The old compass has overshot a little... turn East and try again.")
                play_again()
            else:
                print("You're not quite there yet Sherlock, do try again.")
        else:
            print("Your Gemologist training is a little lacking... back to the lab to learn the cutting process again")
            play_again()
    else:
        print("You're not ready for this important mission. Go back and learn the refining process and and try again next year Goldsmith.")
        play_again()
        
