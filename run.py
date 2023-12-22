# function for creating grid
def create_grid(size):
    return[['-' for _ in range(size)]for _ in range (size)]

# function for printing grid
def print_grid(grid):
    for row in(grid):
        print(" | ". join(row))

# function for placing ships on griddef put_ships():

# function for player guessing ships locationdef player_guess():

target_grid = create_grid(9)
print_grid(target_grid)