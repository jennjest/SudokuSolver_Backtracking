# Sudoku Solver
This repository contains a Python-based Sudoku solver that utilizes the powerful backtracking algorithm to find solutions for any valid Sudoku puzzle.

## 🌟 Overview
The Sudoku Solver is a command-line application designed to efficiently solve standard 9x9 Sudoku puzzles. It takes an incomplete Sudoku grid as input and outputs the complete, solved grid. This project serves as a practical demonstration of the backtracking algorithm, a fundamental technique in computer science for solving problems recursively by trying to build a solution incrementally and removing those solutions that fail to satisfy the constraints of the problem.

## ✨ Features
1. **Efficient Backtracking Algorithm**: Implements a robust backtracking algorithm to explore possible solutions.

2. **Input Flexibility**: Accepts Sudoku puzzles as a 2D list (or similar structure) in Python.

3. **Clear Output**: Prints the solved Sudoku grid in a readable format.

4. **Constraint Checking**: Includes functions to check if a number is valid in a given row, column, or 3x3 subgrid.

## 🛠️ Technologies Used
Python 3.13.5

## 🚀 How to Run
1. Clone the repository:

    git clone https://github.com/jennjest/SudokuSolver_Backtracking.git

    cd SudokuSolver_Backtracking
   
2. Open the Python file:
   Locate the main Python script (e.g., sudoku_backtracking.py or similar) in the cloned directory.

3. Modify the puzzle (optional):
   Inside the script, you'll likely find a variable holding the initial Sudoku grid (often represented as a 2D list). You can modify this grid to test different puzzles. Use 0 (or None) to represent empty cells.

Example puzzle structure:

example_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


Run the script:
Execute the Python script from your terminal:

python sudoku_backtracking.py


(Replace sudoku_backtracking.py with the actual name of your script.)

## 💡 How the Backtracking Algorithm Works
The core of this solver is the backtracking algorithm. Here's a simplified explanation:

Find an Empty Cell: The algorithm starts by searching for the next empty cell (represented by 0).

Try Numbers: For that empty cell, it attempts to place numbers from 1 to 9.

Check Validity: Before placing a number, it checks if that number is valid according to Sudoku rules (not present in the same row, column, or 3x3 subgrid).

Recurse: If a number is valid, it places it and then recursively calls itself to solve the rest of the puzzle.

Backtrack: If the recursive call returns False (meaning no solution was found with the current number), it "backtracks" by removing the number from the current cell and trying the next possible number. If all numbers from 1-9 have been tried and none lead to a solution, it returns False to the previous recursive call.

Solution Found: If all cells are filled and valid, a solution has been found, and the algorithm returns True.

This process continues until a valid solution is found or all possibilities have been exhausted.

## 🤝 Contributing
Feel free to fork this repository, open issues, or submit pull requests if you have suggestions for improvements or bug fixes!
