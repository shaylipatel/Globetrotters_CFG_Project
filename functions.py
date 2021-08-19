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
        # there was a circular dependency issue with this if statement - start() function can only be accessed within
        # this module only by placing import statement within the if statement otherwise logic won't work
        from main import start
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        print('Goodbye!')
        exit()

        

from tkinter import *

def graphics_box():
    #key down function
    def click():
        entered_text=textentry.get().title().strip()  # this will collect the text from the text box
        output.delete(0.0, END)
        try:
            definition = my_compdictionary[entered_text]
        except:
            definition = "sorry there is no such location, please try again"
        output.insert(END, definition)
    ##### main:
    window = Tk()
    window.title("Where is Ada Lovalace?")
    window.configure(background="black")
    #### My Photo
    photo1 = PhotoImage(file="globe.gif")
    Label (window, image=photo1,bg="black") .grid(row=0, column=0, sticky=N)
    #create label
    Label (window, text="Which location would you like to go to?", bg="black",  fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=N)
    #create text entry box
    textentry = Entry(window, width=20, bg="white")
    textentry.grid(row=2, column=0, sticky=N)
    #add a submit button
    Button(window, text="SUBMIT", width=6, command=click) .grid(row=3, column=0, sticky=N)
    #create another label
    Label (window, text="\nClue:", bg="black",  fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=N)
    # create an output text box
    output = Text(window, width=40, height=6, wrap=WORD, background="white")
    output.grid(row=5, column=0, columnspan=2, sticky=N)
    #the dictionary
    my_compdictionary = { #need to connect dictionary to clues dictionaries, and base it on choice of location
        'Buckingham Palace': 'It is one of only three surviving city-states in the world',
        'Tower Of London':'Bukit Timah Nature Reserve holds more species of trees than the entire North American continent',
        'London Eye': 'The national language is Malay'
        }
    #exit label
    Label (window, text="click to exit", bg="black",  fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=N)
    #exit function:
    def close_window():
        window.destroy()
        exit()
    #exit button:
    Button(window, text="Exit", width=14, command=close_window) .grid(row=7, column=0, sticky=N)
    #run the main loop
    return window.mainloop()

graphics_box()

