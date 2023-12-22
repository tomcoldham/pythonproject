import random
# function for creating grid
def create_grid(size):
    return[['-' for _ in range(size)]for _ in range (size)]

# function for printing grid
def print_grid(grid):
    for row in(grid):
        print(" | ". join(row))

# function for placing ships on grid with random number generator
def put_ships(grid):
    for target in range(no_of_ships):
        target_row, target_column = random.randint(0, 8), random.randint(0, 8)
        grid[target_row][target_column] = 'X'

# function for player guessing ships location
def player_guess():
    row_guess = int(input("please enter target guess row number: " ))
    column_guess = int(input("please enter target guess column number: " ))
    return row_guess,column_guess

target_grid = create_grid(9)
no_of_ships = 5
put_ships(target_grid)
print_grid(target_grid)
player_guess()