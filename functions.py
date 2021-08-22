# from main import start
# from main import play_again
from tkinter import *

# warm up exercise
def introduction_qs():
    welcome()
    name = str(input('Please input your name: Agent '))
    answer = input("\nAgent " + name.title() + ", the first item required for this game of wits is COURAGE. \nDo you have a heart of solid gold and are you ready to take on the search for Ada Lovelace? (yes/no) ")
    
    if answer.lower().strip() == 'yes' or answer.lower().strip() == 'y':
        answer = input(("\nExcellent! A half-worthy candidate. \nThe second item required for this mission is an INTELLECT as sharp as the Kohinoor diamond.\nIs this something you possess young Philosopher? (yes/no) "))
        
        if answer.lower().strip() == 'yes' or answer.lower().strip() == 'y':
            answer = input("\nThe first thing to determine is where the trail starts... \nWhere would the world's first computer programmer start her journey... and so where should you? London, New York or Paris? \n")
            
            if answer.lower().strip() == 'london':
                # Correct location
                print("\nExcellent choice! Proceed to London and begin the searching process... the clues are waiting... no dilly-dally-ing.")
                # PROCEED TO BASE_LOCATION
            elif answer.lower().strip() == 'new york':
                # Wrong location
                print("\nThe old compass has overshot a little... turn East and try again.")
                play_again()
            elif answer.lower().strip() == 'paris':
                # Wrong location
                print("\nThe old compass has overshot a little... head 350km North-West and try again.")
                play_again()
               
            else: 
                # If user enters a location which was not listed, the game exits.
                print("\nYou're not quite there yet Sherlock, do try again.")
                exit()
        else:
            print("\nYour Gemologist training is a little lacking... back to the lab to learn the cutting process again.")
            play_again()
    else:
        print("\nYou're not ready for this important mission. Go back and learn the refining process and and try again next year Goldsmith.")
        play_again()

def welcome():
    return print("Welcome to the mission.")

# Function to asks the user if they want to play again.
def play_again():
    print("\nDo you want to play again? (yes/no)")
        # convert the player's input to lower_case
    answer = input(">").lower()

    if answer == 'y*' or answer == 'yes':
        # if player typed "yes" or "y" start the game from the beginning
        # there was a circular dependency issue with this if statement - start() function can only be accessed within
        # this module only by placing import statement within the if statement otherwise logic won't work
        affirmation()
        from main import start
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        print('\nFarewell! We look forward to working with you on another mission.')
        exit()

def affirmation():
    return print('\nGood choice!')


# final function once player has found the correct location
def winners_graphics_box():
    # key down function
    def click():
        entered_text = textentry.get().title().strip()  # this will collect the text from the text box
        output.delete(0.0, END)
        try:
            definition = my_compdictionary[entered_text]
        except:
            definition = "O Greedy One, there is no such treasure! Choose from RUBY, EMERALD or SAPPHIRE"
        output.insert(END, definition)
    ##### main:
    window = Tk()
    window.title("Where is Ada Lovalace?")
    window.configure(background="black")
    #### My Photo
    photo1 = PhotoImage(file="globe.gif")
    Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=N)
    # create label
    Label(window, text="CONGRATULATIONS!!! \nYou have traversed the world and found Ada Lovelace! An Agent worthy of the digits 007.", bg="black", fg="white", font="none 16 bold").grid(row=1, column=0, sticky=N)
    Label(window, text="Choose a jewel from Ada's treasure chest of knowledge. Input your choice of RUBY, EMERALD or SAPPHIRE below:", bg="black", fg="white", font="none 10 bold").grid(row=2, column=0, sticky=N)
    # create text entry box
    textentry = Entry(window, width=30, bg="white")
    textentry.grid(row=3, column=0, sticky=N)
    # add a submit button
    Button(window, text="SUBMIT", width=6, command=click).grid(row=4, column=0, sticky=N)
    # create another label
    Label(window, text="Ada bestows the following great wisdom upon you:", bg="black", fg="white", font="none 16 bold").grid(row=5, column=0, sticky=N)
    # create an output text box
    output = Text(window, width=90, height=8, wrap=WORD, background="white")
    output.grid(row=6, column=0, columnspan=2, sticky=N)
    # the dictionary
    my_compdictionary = {
        'Ruby': 'Don’t Sacrifice Readability:  Whenever you’re writing a piece of code, you should think about what the next developer is going to find when looking at that piece of code. Write that piece of code with the mentality to make it easily understandable and as readable as you can. The ratio of time spent reading code versus writing code is well over 10-to-1. This means that you can save a lot of time in the long run by putting in a little more effort into making your code readable. In order to write readable code try to keep it as simple as possible. Write simple code that everyone can understand.',
        'Emerald': 'Focus On The Business: Some developers are only interested in the technical aspects of their job. They don’t care about the business or the economic factors that justify their job’s existence. Other developers tend to be so focused on learning the tech stack that the business gets out of sight. It’s important to keep the business in mind. Why are you building this? Is what you’re working on creating value for the business or are you spending too much time on something that doesn’t really matter? It’s an important question that you should keep asking yourself.',
        'Sapphire': 'Don’t Dive Straight Into the Code: Rushing into the code might seem exciting at first. However, that excitement might end up costing you a lot of time. When jumping straight into the coding part, you’ll eventually lose sight of the bigger picture. You need to plan and organize before you start coding. Think about problems that you might find along the way and how can you tackle them. How will you structure your code? What’s the reason that you’re going to implement this feature? These questions can make you more aware of the fact that there’s a lot to think about before writing code.'
    }
    # exit label
    Label(window, text="Go forth boldly, O Wise One", bg="black", fg="white", font="none 12 bold").grid(row=7, column=0, sticky=N)
    Label(window, text="click to exit", bg="black", fg="white", font="none 10 bold").grid(row=8, column=0, sticky=N)
    # exit function:
    def close_window():
        window.destroy()
        exit()
    # exit button:
    Button(window, text="Exit", width=14, command=close_window).grid(row=9, column=0, sticky=N)
    #####run the main loop
    return window.mainloop()


