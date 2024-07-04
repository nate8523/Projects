import random

# -------------------------- INPUT PARSING --------------------------

def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    input_string = input_string.strip()
    if input_string.isdigit() and 1 <= int(input_string) <= 6:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

# -------------------------- DICE ROLLING --------------------------

def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    return [random.randint(1, 6) for _ in range(num_dice)]

# -------------------------- ASCII ART DICTIONARY --------------------------

# Dictionary containing ASCII art for each face of a die
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

# Constants for dice dimensions
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

# -------------------------- DIAGRAM GENERATION --------------------------

def generate_dice_faces_diagram(dice_values):
    """Return an ASCII diagram of dice faces from `dice_values`.

    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:

    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    # Create a list of dice faces using the dice values
    dice_faces = [DICE_ART[value] for value in dice_values]

    # Create rows of dice faces
    dice_faces_rows = [
        DIE_FACE_SEPARATOR.join(die[row_idx] for die in dice_faces)
        for row_idx in range(DIE_HEIGHT)
    ]

    # Create the diagram header
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    # Combine the header and dice faces into one string
    return "\n".join([diagram_header] + dice_faces_rows)

# -------------------------- MAIN PROGRAM --------------------------

if __name__ == "__main__":
    # 1. Get and validate user's input
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    num_dice = parse_input(num_dice_input)

    # 2. Roll the dice
    roll_results = roll_dice(num_dice)

    # 3. Generate the ASCII diagram of dice faces
    dice_face_diagram = generate_dice_faces_diagram(roll_results)

    # 4. Display the diagram
    print(f"\n{dice_face_diagram}")