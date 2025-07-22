# KenBoi's Sudoku

This is a Sudoku game application built with Python and the `customtkinter` library. It provides a graphical user interface to play, solve, and validate Sudoku puzzles with customizable difficulty levels.

## Features

*   **Generate Puzzle**: Creates a new random Sudoku puzzle with adjustable difficulty.
*   **Difficulty Slider**: Customize puzzle difficulty by selecting how many cells to remove (20-55 cells).
*   **Hint System**: Get up to 5 hints per puzzle to help you solve challenging spots.
*   **Solve**: Automatically solves the current puzzle on the board.
*   **Clear**: Clears all entries from the grid and resets hint counter.
*   **Validate**: Checks the current state of the puzzle and highlights correct (green) and incorrect (red) entries.
*   **Sleek UI**: A modern and user-friendly dark-themed interface with visual feedback.

## How to Play

1. **Generate a Puzzle**: Click "Create Puzzle" to generate a new Sudoku puzzle.
2. **Adjust Difficulty**: Use the difficulty slider to control how many cells are removed (20-55). More removed cells = harder puzzle.
3. **Fill in Numbers**: Click on empty cells and enter numbers 1-9.
4. **Get Hints**: Click the circular "Hint" button to reveal a correct number in a random empty cell (max 5 hints per puzzle).
5. **Validate**: Click "Validate" to check your current entries - correct numbers will be highlighted in green, incorrect ones in red.
6. **Solve**: Click "Solve" to automatically complete the puzzle.
7. **Clear**: Click "Clear" to start over with a blank grid.

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
