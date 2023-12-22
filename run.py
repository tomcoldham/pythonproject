import random
# function for creating grid
def create_grid(size):
    return[['-' for _ in range(size)]for _ in range (size)]

# function for printing grid
def print_grid(grid):
    for i, row in enumerate(grid, start=1):
        print(f"{i} | {' | '.join(row)}")
    
# function for placing ships on grid with random number generator
def put_ships(grid):
    for target in range(no_of_ships):
        target_row, target_column = random.randint(0, 8), random.randint(0, 8)
        grid[target_row][target_column] = 'X'

# function for player guessing ships location
def player_guess():
    row_guess = int(input("please enter target guess row number: " ))
    column_guess = int(input("please enter target guess column number: " ))
# subtract from guess as grid starts from 0
    row_guess -= 1
    column_guess -= 1
    return row_guess,column_guess

target_grid = create_grid(9)
player_grid = create_grid(9)
no_of_ships = 5
put_ships(target_grid)
print_grid(target_grid)
player_try=player_guess()
if player_grid[player_try[0]][player_try[1]] == 'X':
    print("You have already sunk this ship!")
elif player_grid[player_try[0]][player_try[1]] == 'O':
    print("You have already tried this co-ordinate")
elif target_grid[player_try[0]][player_try[1]] == 'X':
    print("Target hit!")
    player_grid[player_try[0]][player_try[1]] = 'X'
else:
    print("Target missed!")
    player_grid[player_try[0]][player_try[1]] = 'O'

print('    1   2   3   4   5   6   7   8   9')
print_grid(player_grid)