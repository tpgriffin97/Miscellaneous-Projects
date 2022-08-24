# Dice roll application

import time
import random

# Store the dice art within a dictionary using {}, whereas a list used []
DICE_ART = {
    1: (

        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",

    ),
    2: (

        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",

    ),
    3: (

        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",

    ),
    4: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",

    ),
    5: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",

    ),
    6: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),

}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def generate_dice_faces_diagram(dice_values):
    # generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = ' RESULTS '.center(width, '~')

    dice_faces_diagram = '\n'.join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


def parse_input(input_string):
    # Define our function as parse_input and accept the input_string variable as an argument

    # Strip the input_string variable and check to see if it's within the dictionary and is 1,2,3,4,5,6
    if input_string.strip() in {'1', '2', '3', '4', '5', '6'}:
        # If the string is in fact 1-6, convert it to an integer
        return int(input_string)
    else:
        # Request the user only enter a valid number
        print("Please enter a number from 1 to 6 only!")
        time.sleep(3)
        raise SystemExit(1)


def roll_dice(dice_input):
    # Pass dice_input as an argument

    # Dice_input is validated by the parse function, and is now passed to the roll_dice function
    # Parse through the dice_input argument and select a random int
    # Return roll int to the roll_results list
    roll_results = []
    for _ in range(dice_input):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


# ~~ App's Main Code Block ~~

# 1. Get and validate the user's input
user_dice_input = input("How many dice would you like to roll? [1-6]")
dice_input = parse_input(user_dice_input)

# 2. Roll the dice
roll_results = roll_dice(dice_input)

# 3. Generate the ASCII diagram of the dice faces
dice_face_diagram = generate_dice_faces_diagram(roll_results)

# 4. Display the diagram
print(f"\n{dice_face_diagram}")
