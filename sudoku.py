import customtkinter as ck
from sudoku_maker import generate_complete_grid, remove_numbers
from sudoku_solver import solve, is_valid
from PIL import Image

ck.set_appearance_mode("System")
ck.set_default_color_theme("blue")
app = ck.CTk()
app.geometry("700x600")
app.title("KenBoi's Sudoku")

app.iconbitmap("sudoku_logo.ico")


heading_font = ck.CTkFont(family="Helvetica", size=32, weight="bold")


heading = ck.CTkLabel(
    app,
    text="SUDOKU SOLVER",
    font=heading_font,
    text_color="#FFFFFF",
    fg_color="#3b8ed0",
    corner_radius=8,
    padx=20,
    pady=10
)

heading.pack(pady=20)



entry_grid = [[None for i in range(9)] for j in range(9)]
frames = ck.CTkFrame(app)
frames.pack(pady=20)


for i in range(9):
    for j in range(9):
        entry=ck.CTkEntry(frames,
                           width=40,
                           height =40,
                           justify="center",
                           font=("Arial", 20))

        x = (10,2) if j%3==0 and j!=0 else 2
        y = (10,2) if i%3==0 and i!=0 else 2

        entry.grid(row=i,
                   column=j,
                   padx= x,
                   pady = y)
    
    
        entry_grid[i][j] = entry
    

def get_from_entries():
    grid = []
    for i in entry_grid:
        grid.append([int(j.get()) if j.get().isdigit() else 0 for j in i])
    
    return grid

def set_grid(grid, locked=None):
    for i in range(9):
        for j in range(9):
            value = grid[i][j]
            enter = entry_grid[i][j]
            enter.configure(border_color="grey", border_width=1, state="normal")
            entry_grid[i][j].delete(0,"end")


            if value != 0:
                enter.insert(0, str(value))
                if locked and (i,j) in locked:
                    entry_grid[i][j].configure(state="disabled")
                else:
                    enter.configure(state="normal")

def generate():
    full = generate_complete_grid()
    puzzle = remove_numbers(full)



    locked = [(i, j) for i in range(9) for j in range(9) if puzzle[i][j] != 0]


    set_grid(puzzle, locked=locked)


def solve_sudoku():
    grid = get_from_entries()
    solve(grid)
    set_grid(grid)


def clear():
    for i in entry_grid:
        for j in i:
            j.configure(state="normal")
            j.delete(0,"end")
            j.configure(border_color="grey", border_width=1)

def validate():
    grid = get_from_entries()
    for i in range(9):
        for j in range(9):
            value = grid[i][j]
            if value ==0:
                continue
            grid[i][j] = 0


            if not is_valid(value, (i,j), grid):
                entry_grid[i][j].configure(border_color="red", border_width=2)
            else:
                entry_grid[i][j].configure(border_color="green", border_width=2)

            grid[i][j] = value




frame_1 = ck.CTkFrame(app)
frame_1.pack(pady= 10)

button_1 = ck.CTkButton(frame_1,
                        text="Create Puzzle",
                        command = generate)

button_1.grid(row=0,
              column=0, 
              padx=5)


button_2 = ck.CTkButton(frame_1,
                        text="Solve",
                        command = solve_sudoku)

button_2.grid(row=0,
              column=1, 
              padx=5)


button_3 = ck.CTkButton(frame_1,
                        text="Clear",
                        command = clear)

button_3.grid(row=0,
              column=2,
              padx=5)



button_4 = ck.CTkButton(frame_1,
                        text="Validate",
                        command = validate)

button_4.grid(row=0,
              column=3,
              padx=5)

app.mainloop()