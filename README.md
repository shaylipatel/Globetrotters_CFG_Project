# Where is Ada Lovelace? A text adventure game  (Globetrotters_CFG_Project)

**Name**
Where is Ada Lovelace? A text adventure game.

**Description**
This is a walk-through text adventure game in Python. The objective of the game has the player travel to a city where they can find up to 3 clues at different landmarks, which direct them to the next location the protagonist, Ada Lovelace, has moved on to. It is considered a popular mystery exploration game, known to be a great way for the player to test out their location-specific trivia skills throughout the game. We took our inspiration from the 1985 computer game ‘Where on Google Earth is Carmen Sandiago?’ We also noticed that Google Earth have also created their own version of this game: https://tinyurl.com/4xw8mxmr

**Visuals**
This game is almost entirely a text game, as the user is walked through the game with instructions, humour and clues.
**[image]**(https://user-images.githubusercontent.com/75260092/130352811-03968a62-c8df-4165-a760-689cd41313ac.png)

**Requirements**
1.	This game has been designed for Python 3 and will only run in Python 3.
2.	This game requires and API key from https://openweathermap.org/ - full details in installation.
3.	Installation of Python packages ‘colorama’ and ‘tkinter’ (tkinter is pre-installed with Python 3)

**Installation**
1.	Clone the files from GitHub to your local directory
2.	Install colorama within python if you do not already have this – within the terminal on your machine, type: pip install colorama
3.	You will need an API key. Register at: https://openweathermap.org/ 
4.	Once you have an API key, paste this in the config.py file. The file makes clear where this needs to go. Do not change anything else in the file.
5.	In the functions.py file, revert the url under the get_weather function back to this:
url = f"https://api.openweathermap.org/data/2.5/weather?q={self.name}&appid={config.api_key}&units=metric"
6.	Go to the main.py file and run the game.

**Authors** 
Michaela D’Mello, Nosheen Masud, Lana Moroney, Shayli Patel and Catherine Phillips.

**License**
This project is open source and all ownership rights are attributed to the authors.

**Project status**
This game was created as a final project for a bootcamp on software engineering.  Development has stopped completely as we have submitted our project. 
 
