
class Location:

    def __init__(self, name, coordinates, country, timezone, languages, GDP, landmarks, clues):
        self.name = name
        self.coordinates = coordinates
        self.country = country
        self.timezone = timezone
        self.languages = languages
        self.GDP = GDP
        self.landmarks = landmarks
        self.clues = clues


    def location_facts(self):
        print("Facts about {} \nCoordinates: {} \nCountry: {} \nTime Zone: {} \nLanguages: {} \nGDP Per Capita: US ${}".format(self.name, self.coordinates, self.country, self.timezone, self.languages,self.GDP))
    def next_location(self, location_list, correct_location,incorrect_landmarks1,incorrect_landmarks2):
        self.location_list = location_list
        self.correct_location = correct_location
        self.incorrect_landmarks1 = incorrect_landmarks1
        self.incorrect_landmarks2 = incorrect_landmarks2

# correct route location info
London = Location(
    "London",
    "51°30′26″N 0°7′39″W",
    "United Kingdom",
    "UTC00 (Greenwich Mean Time)",
    "English",
    78001,
    ['1. Buckingham Palace ', '2. Tower of London ', '3. London Eye '],
    {1: 'It is one of only three surviving city-states in the world ',
    2:'Bukit Timah Nature Reserve holds more species of trees than the entire North American continent.',
    3: 'The national language is Malay.'}
    )

Singapore = Location(
    "Singapore",
    "1°17′N 103°50′E",
    "Singapore",
    "UTC+8 (Singapore Standard Time)",
    "English, Malay, Mandarin, Tamil",
    102742,
    ['1. Supertree Grove ',	'2. Gardens by the Bay ', '3. Marina Bay Sands '],
    {1:'It is the home of one largest and most prominent LGBT communities in the country.' ,
    2: 'It has a famous Island that lies in the bay, Alkatraz is its name. ',
    3:'In this location, suspended high in the sky and painted red as the colour of extremes...a bridge that is one of the wonders of the modern world and longest in the world' }
    )
San_Fran = Location(
    "San Francisco",
    "37°46′39″N 122°24′59″W",
    "United States of Amereica",
    "UTC−8 (Pacific Time Zone)",
    "English",
    230829,
    ['1. Golden Gate Bridge ', '2. Alkatraz Island ', '3. Golden Gate Park '],
    {1: 'A great Fotre is housed in this majestic city',
    2: 'The second most populated city in the world',
    3: 'Home to the largest market of spices in Asia'}
    )
Delhi = Location(
    "Delhi",
    "28°36′36″N 77°13′48″E",
    "India",
    "UTC+5.30 (India Standard Time)",
    "Hindi, English, Punkabi, Urdu",
    7900,
    ['India Gate','Qutub Minar','Humayun\'s Tomb'],
    {1: 'Hosts one of the oldest universities in the world, founded in 975 CE',
     2: 'The largest city in Africa and the Middle East',
     3: 'Home to the only remaining ancient wonder of the world'}
    )

Cairo = Location(
    "Cairo",
    "30°2′N 31°14′E",
    "Egypt",
    "UTC+2 (Egypt Standard Time)",
    "Arabic",
    3587,
    ['Pyramids of Giza','Great Sphinx',	'Coptic Cairo'],
    {1: 'They were seen earlier today in Old Cairo!',
     2: 'They were seen in the historic district of Cairo',
     3: 'You have found Ada Lovelace!'}
    )

# incorrect location info
incorrect_location_clues = {1: 'I haven\'t seen who you are looking for',
                                 2: 'I don\'t know what you are talking about',
                                 3: 'You are in the wrong place, buddy!'}
Barca = Location(
    'Barcalona',
    '41.3851°N, 2.1734°E',
    'Spain',
    'UTC+2 (Central European Summer Time)',
    'Catalan, Spanish',
    29600,
    ['Basilica of the Sagrada Familia','Casa Batllo','Palace of Catalan Music'],
    incorrect_location_clues
)

Reykjavik = Location(
    'Reykjavik',
    '64.1466° N, 21.9426° W',
    'Iceland',
    'UTC00 (Greenwich Mean Time)',
    'Icelandic',
    66945,
    ['Perlan','Hallgrimskirkja','Videy Island'],
    incorrect_location_clues
)

Rio = Location(
    'Rio de Janeiro',
    '22.9068° S, 43.1729° W',
    'Brazil',
    'UTC-3 (Brasilia Standard Time)',
    'Brazilian Portuguese',
    11032,
    ['Christ the Redeemer','Copacabana','Ipanema'],
    incorrect_location_clues
)

Tokyo = Location(
    'Tokyo',
    '35.6762° N, 139.6503° E',
    'Japan',
    'UTC+09:00 (Japan Standard Time)',
    'Japanese',
    40247,
    ['Tokyo National Museum','Senso-ji Temple','Tokyo Skytree'],
    incorrect_location_clues
)

# choice tree
# First Location Choice
London.next_location(
    [Singapore, London, Barca, Rio],
    'Singapore',
    Barca,
    Rio
)

# Second Location Choice
Singapore.next_location(
    [San_Fran, Singapore,Reykjavik,Tokyo],
    'San Francisco',
    Reykjavik,
    Tokyo
)

# Third Location Choice
San_Fran.next_location(
    [Delhi, Singapore, Tokyo, Barca ],
    'Delhi',
    Tokyo,
    Barca
)

# Fourth Location Choice
Delhi.next_location(
    [Cairo, Delhi, Rio, Reykjavik],
    'Cairo',
    Rio,
    Reykjavik
)


correct_route = [London, Singapore, San_Fran, Delhi, Cairo]

# for location in correct_route:
#     print(location.name)
#     for landmark in location.landmarks:
#         print(landmark)
#     print(location.location_facts())
