import random
import copy
from itertools import product

def is_valid(num, position, grid):
    # This is used to check the rows
    for i in range(len(grid[0])):
        if grid[position[0]][i] == num and position[1] != i:
            return False

    # This is used to check the column
    for i in range(len(grid)):
        if grid[i][position[1]] == num and position[0] != i:
            return False

    # This is used to check the inner box.
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i,j) != position:
                return False

    return True

def solve(grid):
    
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)  # Randomize to create different numbers
                
                for num in numbers:
                    if is_valid(num, (i, j), grid):
                        grid[i][j] = num
                        
                        if solve(grid):
                            return True
                        
                        grid[i][j] = 0
                
                return False
    return True

def generate_complete_grid():
    
    grid = [[0 for _ in range(9)] for _ in range(9)]
    
    # Filling the diagonals becuase they don't intercept with eachother
    for box in range(0, 9, 3):
        fill_box(grid, box, box)
    
    # Filling remaining cells
    solve(grid)
    return grid

def fill_box(grid, row, col):
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    
    for i in range(3):
        for j in range(3):
            grid[row + i][col + j] = numbers[i * 3 + j]

def remove_numbers(grid, num_to_remove=30):
    
    new_grid = [row[:] for row in grid]
    
    # Getting the coordinates
    cells = list(product(range(9), range(9)))
    

    random.shuffle(cells)
    
    for i in range(num_to_remove):
        row, col = cells[i]
        new_grid[row][col] = 0
        
    return new_grid

def print_grid(grid):
    
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ") 

            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

def generate_sudoku_puzzle():
    print("Generating Sudoku puzzle...")
    
    complete_grid = generate_complete_grid()
    
    
    puzzle = remove_numbers(complete_grid)
    
    print("\nSudoku Puzzle:")
    print_grid(puzzle)
    
    # Ask the user if they want to generate a new puzzle
    
    if generate == 'y':
        # Generate a new puzzle
        grid = generate_complete_grid()
    
    return puzzle, complete_grid

def main():
    print("=== SUDOKU PUZZLE GENERATOR ===")
    
    while True:
        generate = input("\Do you want to generate a new puzzle? (y/n): ").lower().strip()
        
        if generate == 'n':
            print("Thanks for using KenBoi's Sudoku!")
            break
        elif generate == 'y':
            puzzle, solution = generate_sudoku_puzzle()
        else:
            print("Please enter 'y' or 'n'")

if __name__ == "__main__":
    main()