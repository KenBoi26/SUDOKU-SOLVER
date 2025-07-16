# KenBoi's Sudoku

This is a Sudoku game application built with Python and the `customtkinter` library. It provides a graphical user interface to play, solve, and validate Sudoku puzzles.

## Features

*   **Generate Puzzle**: Creates a new random Sudoku puzzle.
*   **Solve**: Automatically solves the current puzzle on the board.
*   **Clear**: Clears all entries from the grid.
*   **Validate**: Checks the current state of the puzzle and highlights correct and incorrect entries.
*   **Sleek UI**: A modern and user-friendly interface.

## How to Run

1.  **Prerequisites**: Make sure you have Python installed on your system.

2.  **Install Dependencies**: Open a terminal or command prompt in the project directory and install the required libraries:
    ```bash
    pip install customtkinter pillow
    ```

3.  **Run the Application**: Execute the main script to start the game:
    ```bash
    python sudoku.py
    ```

## Files

*   `sudoku.py`: The main application file that runs the GUI.
*   `sudoku_maker.py`: Contains the logic for generating new Sudoku puzzles.
*   `sudoku_solver.py`: Contains the algorithm to solve the Sudoku puzzles.
*   `sudoku_logo.ico`: The icon for the application window.
