import random
import time
import math

# function for creating grid
def create_grid(size):
    return[['-' for _ in range(size)]for _ in range (size)]

# function for printing grid
def print_grid(grid):
    header = "-   " + "   ".join(map(str, range(1, len(grid) + 1)))
    print("\033[1;34m" + header + "\033[0m")
    for i, row in enumerate(grid, start=1):
        print(f"\033[1;34m{i}\033[0m | {' | '.join(row)}")
    
# function for placing ships on grid with random number generator, based on size of grid
def put_ships(grid):
    random.seed(time.time())
    for target in range(no_of_ships):
        target_row, target_column = random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)
        grid[target_row][target_column] = 'X'
        while grid[target_row][target_column] == 'X':
            target_row, target_column = random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)
        grid[target_row][target_column] = 'X'

# function for player guessing ships location (rows)
def player_guessrow():
    valid_row = False
    while not valid_row:
        try:
            row_input =(input("""

Please enter target guess row number: """))
            if row_input.lower() == "quit":
                exit()
            row_guess = int(row_input)
        except ValueError:
            print("Invalid input, please enter a number or quit")
        else: 
            if 1 <= row_guess <= grid_size:
                valid_row = True
                return row_guess -1
            else:
                print("Number not in range")

# function for player guessing ships location (columns)
def player_guesscol():
    valid_col = False
    while not valid_col:
        try:
            col_input =(input("""
Please enter target guess column number: """))
            if col_input.lower() == "quit":
                exit()
            col_guess = int(col_input)
        except ValueError:
            print("""
            Invalid input, please enter a number or quit
            """)
        else: 
            if 1 <= col_guess <= grid_size:
                valid_col = True
                return col_guess -1
            else:
                print("""
                number not in range
                """)

#main function to play the game
def play_game():
    global no_of_ships, no_of_attempts, no_of_hits, grid_size, player_grid
#allows player to chose a grid size
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
    no_cells = grid_size * grid_size
#allows player to select difficulty level with varying number of shots
    choose_level = ["1", "2", "3"]
    selection = input("Input your diffculty level: Beginner (1), Intermediate (2), Advanced (3): ")
    while selection not in choose_level:
        selection = input("Input your diffculty level: Beginner (1), Intermediate (2), Advanced (3): ")
    else:
        level = int(selection)
    if level == 1:
        attempts = (90 / 100) * no_cells
        no_of_attempts = math.ceil(attempts)
    if level == 2:
        attempts = (70 / 100) * no_cells
        no_of_attempts = math.ceil(attempts)
    if level == 3:
        attempts = (50 / 100) * no_cells
        no_of_attempts = math.ceil(attempts)
#setup the grids on the terminal
    target_grid = create_grid(grid_size)
    player_grid = create_grid(grid_size)
    percent_ships = (30 / 100) * no_cells
    no_of_ships = math.ceil(percent_ships)
    no_of_hits = 0
    put_ships(target_grid)
    print(f"You have {no_of_ships} battleships to sink!")
#loops for playing game depending on number of attempts and ships left
    while no_of_attempts > 0:
        if no_of_hits == no_of_ships:
            break
        print_grid(player_grid)
        player_try_row=player_guessrow()
        player_try_col=player_guesscol()
        if player_grid[player_try_row][player_try_col] == 'X':
            print(f"""
You have already hit this ship! you have {no_of_attempts} shots left.""")
        elif player_grid[player_try_row][player_try_col] == 'O':
            print(f"""
You have already tried this coordinate! you have {no_of_attempts} shots left.""")
        elif target_grid[player_try_row][player_try_col] == 'X':
            no_of_attempts -= 1
            print(f"""
Target hit! you have {no_of_attempts} shots left.""")
            no_of_hits += 1
            player_grid[player_try_row][player_try_col] = 'X'
        else:
            no_of_attempts -= 1
            print(f"""
Target Missed! you have {no_of_attempts} shots left.""")
            player_grid[player_try_row][player_try_col] = 'O'

#function to end game once criteria has been met
global no_of_ships, no_of_hits, grid_size, player_grid
def print_endgame():
    print_grid(player_grid)
    if no_of_hits == no_of_ships:
        print(f"Congratulations you have sunk all the ships! If you want to play again type 'start'")
    else:
        print(f"You sunk {no_of_hits} out of {no_of_ships} ships, better luck next time! type 'start' if you wish to play again.")

#menu for user to start game, display instructions or quit
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

The aim of the game is to correctly guess the coordinates
of the computers randomly placed battleship locations.

Simply type a number for the row,then column and 
hit enter to guess a location. 

If you run out of shots before all of the ships are found, you lose. 

If you manage to hit all of the ships before your run out of hits then you win!

The grid size can be altered which will change the ammount of ships, there will
also be a difficulty level that can be selected by the user which changes the 
ammount of shots the user has, the fewer the shots the harder the difficulty!
*****************
""")
    else:
        print("Please enter start, quit or help")