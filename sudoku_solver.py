def is_valid(num, position, grid):
    # Check row
    for i in range(len(grid[0])):
        if grid[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][position[1]] == num and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i,j) != position:
                return False

    return True


def solve(grid):
    zero_cells = [(i,j) for i in range(9) for j in range(9) if grid[i][j] == 0]
    tracker = {}
    position = 0

    while(position < len(zero_cells)):
        i,j = zero_cells[position]
        num = tracker.get((i,j), 0) + 1  # Start from next number after last tried

        found = False
        while(num <= 9):
            if is_valid(num, (i,j), grid):
                grid[i][j] = num
                tracker[(i,j)] = num
                position += 1
                found = True
                break

            num += 1
        
        # if the number is not valid
        if not found:
            grid[i][j] = 0
            if (i,j) in tracker:
                del tracker[(i,j)] # deleting it from the dictionary (like stack)
            position -= 1

            if position < 0:
                print("UNSOLVABLE MY CHILD!")
                return False
        
    print_grid(grid)
    print("THIS IS THE FINAL SOLUTION MY CHILD!!")
    return True




def input_grid():
    l = []

    for i in range(9):
        print("Enter the",i+1,"row. Put an 0 for the empty part.")

        # I have made this code to check whether the input is valid i.e. making sure the user has given me all the numbers for that row

        while(True):
            try:
                row = input("Row",i+1,": ").strip().split()
                if len(row) != 9:
                    raise ValueError("Must enter 9 numbers.") # raising the error
                
                # I am converting the character to a number and appending the row into the main list(i.e. the grid)
                int_row = []
                for i in row:
                    int_row.append(int(i))
                l.append(int_row)
                break
            except ValueError as e: # the error has been called
                print(f"Invalid input: {e}")

    return l

def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ") 

            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()