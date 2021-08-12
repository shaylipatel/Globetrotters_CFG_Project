
def choose_landmark(dict, list):
    while True:
        choice = input('Where would you like to go? ')
        if choice.upper() == 'NEXT':
            break
        elif int(choice) in dict.keys():
            print('{}: {}'.format(list[int(choice)-1],dict[int(choice)]))
def choose_location(list,globe_index):
    while True:
        choice = input('Where would you like to go? ')
        correct_location = globe_index + 1
        if choice == str(list[correct_location]):
            break
        elif choice == globe_index:
            choose_landmark(dict)
#
# London_clues = {
#     1: 'It is one of only three surviving city-states in the world ',
#     2:'Bukit Timah Nature Reserve holds more species of trees than the entire North American continent.',
#     3: 'The national language is Malay.'
# }

London = ['1. Buckingham Palace ', '2. Tower of London ', '3. London Eye ']
Singapore = ['1. Supertree Grove ',	'2. Gardens by the Bay ', '3. Marina Bay Sands ']
San_Fran = ['1. Golden Gate Bridge ', '2. Alkatraz Island ', 	'3. Golden Gate Park ']
# while True:
globe = (London, Singapore, San_Fran) # Delhi, Cairo
correct_route = ['London', 'Singapore', 'San Francisco'] #'Delhi', 'Cairo'

location_choices = [['Singapore','London, UK'], ['San Francisco, USA', 'Singapore'], ['Delhi, India', 'San Francisco, USA']]
London_clues = {1: 'It is one of only three surviving city-states in the world ',
    2:'Bukit Timah Nature Reserve holds more species of trees than the entire North American continent.',
    3: 'The national language is Malay.'}

Singapore_clues = {1:'It is the home of one largest and most prominent LGBT communities in the country.' ,
    2: 'It has a famous Island that lies in the bay, Alkatraz is its name. ',
    3:'In this location, suspended high in the sky and painted red as the colour of extremes...a bridge that is one of the wonders of the modern world and longest in the world' }

San_Fran_clues = {
    1: 'A great Fotre is housed in this majestic city',
    2: 'The second most populated city in the world',
    3: 'Home to the largest market of spices in Asia'
    }

clues = [London_clues, Singapore_clues, San_Fran_clues]

for location in globe:
    globe_index = globe.index(location)
    for landmark in location:
        print(landmark)
    print('To move to the next location, enter NEXT')
    choose_landmark(clues[globe_index], location)
    for location in location_choices[globe_index]:
        print(location)
    choose_location(correct_route,globe_index)
