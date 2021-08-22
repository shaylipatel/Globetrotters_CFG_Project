import requests  # for API
from functions.config1 import api_key


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
        print("Facts about {}: \nCoordinates: {} \nCountry: {} \nTime Zone: {} \nLanguages: {} \nGDP Per Capita: US ${}\nTemperature: {}˚Celsius ".format(self.name, self.coordinates, self.country, self.timezone, self.languages,self.GDP, self.temp))


    def get_weather(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.name}&appid={api_key}&units=metric"
        response = requests.get(url)
        result = response.json()

        for key, value in result.items():
            if key == 'main':
                self.temp = value["temp"]


    def next_location(self, location_list, correct_location,incorrect_landmark1,incorrect_landmark2):
        self.location_list = location_list
        self.correct_location = correct_location
        self.incorrect_landmark1 = incorrect_landmark1
        self.incorrect_landmark2 = incorrect_landmark2

# correct route location info 
# creating objects where we hard code the data for the locations
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
    ['1. India Gate','2. Qutub Minar','3. Humayun\'s Tomb'],
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
    ['1. Pyramids of Giza','2. Great Sphinx',	'3. Coptic Cairo'],
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
    ['1. Basilica of the Sagrada Familia','2. Casa Batllo','3. Palace of Catalan Music'],
    incorrect_location_clues
)

Reykjavik = Location(
    'Reykjavik',
    '64.1466° N, 21.9426° W',
    'Iceland',
    'UTC00 (Greenwich Mean Time)',
    'Icelandic',
    66945,
    ['1. Perlan','2. Hallgrimskirkja','3. Videy Island'],
    incorrect_location_clues
)

Rio = Location(
    'Rio De Janeiro',
    '22.9068° S, 43.1729° W',
    'Brazil',
    'UTC-3 (Brasilia Standard Time)',
    'Brazilian Portuguese',
    11032,
    ['1. Christ the Redeemer','2. Copacabana','3. Ipanema'],
    incorrect_location_clues
)

Tokyo = Location(
    'Tokyo',
    '35.6762° N, 139.6503° E',
    'Japan',
    'UTC+09:00 (Japan Standard Time)',
    'Japanese',
    40247,
    ['1. Tokyo National Museum','2. Senso-ji Temple','3. Tokyo Skytree'],
    incorrect_location_clues
)

# choice tree
# First Location Choice
London.next_location(
    ['Singapore','London, UK', 'Barcalona, Spain','Rio de Janeiro, Brazil'],
    'Singapore',
    Barca,
    Rio
)

# Second Location Choice
Singapore.next_location(
    ['San Francisco, USA', 'Singapore','Reykjavik, Iceland','Tokyo, Japan'],
    'San Francisco',
    Reykjavik,
    Tokyo
)

# Third Location Choice
San_Fran.next_location(
    ['Delhi, India', 'Singapore', 'Tokyo, Japan', "Barcalona, Spain "],
    'Delhi',
    Tokyo,
    Barca
)

# Fourth Location Choice
Delhi.next_location(
    ['Cairo, Egypt', 'Delhi, India', 'Rio de Janeiro, Brazil','Reykjavik, Iceland'],
    'Cairo',
    Rio,
    Reykjavik
)

# get weather
London.get_weather()
Singapore.get_weather()
San_Fran.get_weather()
Delhi.get_weather()
Cairo.get_weather()



correct_route = [London, Singapore, San_Fran, Delhi, Cairo]


# for location in correct_route:
#     print(location.name)
#     for landmark in location.landmarks:
#         print(landmark)
#     print(location.location_facts())

