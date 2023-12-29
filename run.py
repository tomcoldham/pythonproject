import random
import time
# function for creating grid
def create_grid(size):
    return[['-' for _ in range(size)]for _ in range (size)]

# function for printing grid
def print_grid(grid):
    header = "-   " + "   ".join(map(str, range(1, len(grid) + 1)))
    print(header)
    for i, row in enumerate(grid, start=1):
        print(f"\033[1;34m{i}\033[0m | {' | '.join(row)}")
    
# function for placing ships on grid with random number generator
def put_ships(grid):
    random.seed(time.time())
    for target in range(no_of_ships):
        target_row, target_column = random.randint(0, 8), random.randint(0, 8)
        grid[target_row][target_column] = 'X'


# function for player guessing ships location

def player_guessrow():
    valid_row = False
    while not valid_row:
        try:
            row_input =(input("please enter target guess row number: " ))
            if row_input.lower() == "quit":
                exit()
            row_guess = int(row_input)
        except ValueError:
            print("Invalid input, please enter a number or quit")
        else: 
            if 1 <= row_guess <= 9:
                valid_row = True
                return row_guess -1
            else:
                print("number not in range")

def player_guesscol():
    valid_col = False
    while not valid_col:
        try:
            col_input =(input("please enter target guess column number: " ))
            if col_input.lower() == "quit":
                exit()
            col_guess = int(col_input)
        except ValueError:
            print("Invalid input, please enter a number or quit")
        else: 
            if 1 <= col_guess <= 9:
                valid_col = True
                return col_guess -1
            else:
                print("number not in range")

def play_game():
    global no_of_ships, no_of_attempts, no_of_hits
    valid_grid = False
    while not valid_grid:
        try:
            grid_input=(input("Please enter grid size (between 4 and 9) : " ))
            if grid_input.lower() == "quit":
                exit()
            grid_size = int(grid_input)
        except ValueError:
            print("Invalid input, please enter a number of quit")
        else:
            if 4 <= grid_size <= 9:
                valid_grid = True
            else:
                print("Grid size must be between 4 and 9")

    choose_level = ["1", "2", "3"]
    selection = input("Input your diffculty level: Beginner (1), Intermediate (2), Advanced (3) ")
    while selection not in choose_level:
        selection = input("Input your diffculty level: Beginner (1), Intermediate (2), Advanced (3) ")
    else:
        level = int(selection)
    if level == 1:
        no_of_attempts = 70
    if level == 2:
        no_of_attempts = 45
    if level == 3:
        no_of_attempts = 30
    target_grid = create_grid(9)
    player_grid = create_grid(9)
    no_of_ships = 10
    no_of_hits = 0
    put_ships(target_grid)
    while no_of_attempts > 0:
        if no_of_hits == no_of_ships:
            break
        print("\033[1;34m    1   2   3   4   5   6   7   8   9\033[0m")
        print_grid(player_grid)
        player_try_row=player_guessrow()
        player_try_col=player_guesscol()
        if player_grid[player_try_row][player_try_col] == 'X':
            print(f"You have already hit this ship! you have {no_of_attempts} shots left.")
        elif player_grid[player_try_row][player_try_col] == 'O':
            print(f"You have already tried this coordinate! you have {no_of_attempts} shots left.")
        elif target_grid[player_try_row][player_try_col] == 'X':
            no_of_attempts -= 1
            print(f"Target hit! you have {no_of_attempts} shots left.")
            no_of_hits += 1
            player_grid[player_try_row][player_try_col] = 'X'
        else:
            no_of_attempts -= 1
            print(f"Target Missed! you have {no_of_attempts} shots left.")
            player_grid[player_try_row][player_try_col] = 'O'

def print_endgame():
    global no_of_ships, no_of_hits
    if no_of_hits == no_of_ships:
        print(f"Congratulations you have sunk all the ships!")
    else:
        print(f"You sunk {no_of_hits} out of {no_of_ships} ships, better luck next time!")

command = ""
print("""
Welcome to my battleships game!
------------------------------
To start the game type 'start'
------------------------------
To exit the game type 'quit'
------------------------------
If you need a brief tutorial 
on how the game works type 'help'
""")
while True:
    command = input("> ").lower()
    if command == "start":
        play_game()
        print_endgame()
    elif command == "quit":
        exit()
    elif command == "help":
        print("""
*****************
In battleships you will have a certain
ammount of shots to take. 

The aim of the gamee is to correctly guess the coordinates
of the computers randomly placed battleship locations.

Simply type a number for the row,then column and 
hit enter to guess a location. 

If you run out of shots before all of the ships are found, you lose. 

If you manage to hit all of the ships before your run out of hits then you win!

There is also a difficulty level at the start of the game which gives you a choice
of how many attempts you have to win. The less attempts the harder the game.

Difficulty 1 = 70 attempts.

Difficulty 2 = 45 attempts.

Difficulty 3 = 30 attempts.

*****************
""")
    else:
        print("Please enter start, quit or help")