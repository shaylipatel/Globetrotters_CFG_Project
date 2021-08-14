# from main import start
# from main import play_again

# warm up exercise
def introduction_qs():
    name = str(input('Please input your name: Agent '))
    answer = input("Hello Agent " + name.title() + ",the first item required for this game of wits is COURAGE. \nDo you have a heart of solid gold and are you ready to take on the search for Ada Lovelace? (yes/no) ")
    
    if answer.lower().strip() == 'yes' or answer.lower().strip() == 'y':
        answer = input(("Excellent! A half-worthy candidate. \nThe second item required for this mission is an INTELLECT as sharp as the Kohinoor diamond. Is this something you possess young Philosopher? (yes/no) "))
        
        if answer.lower().strip() == 'yes' or answer.lower().strip() == 'y':
            answer = input("The first thing to determine is where the trail starts... \nWhere would the world's first computer programmer start her journey... and so where should you? London, New York or Paris? \n")
            
            if answer.lower().strip() == 'london':
                # Correct location
                print("Excellent choice! Proceed to London and begin the searching process... the clues are waiting... no dilly-dally-ing.")
                # PROCEED TO BASE_LOCATION
            elif answer.lower().strip() == 'new york':
                # Wrong location
                print("The old compass has overshot a little... turn East and try again.")
                play_again()
            elif answer.lower().strip() == 'paris':
                # Wrong location
                print("The old compass has overshot a little... head 350km North-West and try again.")
                play_again()
               
            else: 
                # If user enters a location which was not listed, the game exits.
                print("You're not quite there yet Sherlock, do try again.")
                exit()
        else:
            print("Your Gemologist training is a little lacking... back to the lab to learn the cutting process again.")
            play_again()
    else:
        print("You're not ready for this important mission. Go back and learn the refining process and and try again next year Goldsmith.")
        play_again()

# introduction_qs()


# Function to asks the user if they want to play again.
def play_again():
    print("\nDo you want to play again? (y or n)")

    # convert the player's input to lower_case
    answer = input(">").lower()

    if answer == 'y' or answer == 'yes':
        # if player typed "yes" or "y" start the game from the beginning
        from main import start
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        print('Goodbye!')

