"""Practice Exercise: Game Settings 🎮
In this exercise, you'll use a tuple to store fixed settings for a game. Tuples are ideal here because their immutability prevents accidental changes to settings during gameplay.

The Goal
Your task is to create a tuple for game settings, access its data, and display it.

Step-by-Step Instructions
Setup: In your 02_data_structures/exercises/ folder, create a new file named exercise_tuple_settings.py.

Create the Tuple: Inside the script, define a tuple named game_config. It should store the following information in this exact order: the difficulty level (a string), the screen width (an integer), and the screen height (an integer).

Example: ("Hard", 1920, 1080)

Access and Print: Access each item in the tuple by its index and print them out with descriptive labels.

Example: difficulty = game_config[0]

Try Unpacking (A Cool Trick!): You can "unpack" a tuple to assign all its values to variables in one line. Add this to your script:

Python

# This assigns "Hard" to mode, 1920 to width, and 1080 to height
mode, width, height = game_config
print(f"Unpacked settings: Mode={mode}, Width={width}, Height={height}")

Prove Immutability: Add a comment explaining why you can't change the tuple's values.

Example: # Tuples are immutable, so attempting game_config[0] = "Easy" will result in an error.

Your final output should look like this:

Game Difficulty: Hard
Screen Resolution: 1920x1080
Unpacked settings: Mode=Hard, Width=1920, Height=1080
"""



game_config = ("Hard", 1920, 1080)

# This assigns "Hard" to mode, 1920 to width, and 1080 to height
game_dificulty = game_config[0]
print(f"Game Difficulty: {game_dificulty}")
width = game_config[1]
height = game_config[2]
print(f"screen_Resolution: {width}x{height}")
mode, width, height = game_config
print(f"Unpacked settings: Mode={mode}, Width={width}, Height={height}")

# I can't change the difficulty with game_config[0] = "Easy" because tuples are immutable.