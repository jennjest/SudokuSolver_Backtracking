def solve_sudoku(board):
    # Main function to solve Sudoku using backtracking.
    # Displays the solving steps.

    find = find_empty(board)
    if not find: # If there are no empty cells, the Sudoku is filled
        print("\nALL CELLS FILLED! SOLUTION FOUND.")
        return True
    else:
        row, col = find # Get the position of the next empty cell
        print(f"\nSearching for empty cell at ({row}, {col})...")

    for i in range(1, 10):  # Try numbers from 1 to 9
        print(f"   Trying {i} at ({row}, {col})...")
        if is_valid(board, i, (row, col)):
            board[row][col] = i  # Assign the number if valid
            print(f"     Successfully placed {i} at ({row}, {col}). Moving to the next cell.")
            print_board(board) # Display the board after placement

            if solve_sudoku(board):  # Recurse to the next cell
                return True

            # BACKTRACK: Undo the assignment if recursion fails
            board[row][col] = 0
            print(f"     Failed with {i} at ({row}, {col}). UNDO placement and backtrack.")

    print(f"No valid number for ({row}, {col}). Backtracking further.")
    return False  # No valid number for this cell

def find_empty(board):
    # Finds the next empty cell (value 0) on the Sudoku board.
    # Returns a tuple (row, col) if found, None if none exist.
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def is_valid(board, num, pos):
    # Checks if the number 'num' is valid to be placed at position 'pos'.
    # Pos is a tuple (row, col)

    row, col = pos

    # Check row
    for c in range(9):
        if board[row][c] == num and col != c:
            return False

    # Check column
    for r in range(9):
        if board[r][col] == num and row != r:
            return False

    # Check 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3

    for r in range(box_row_start, box_row_start + 3):
        for c in range(box_col_start, box_col_start + 3):
            if board[r][c] == num and (r, c) != pos:
                return False
    return True

def print_board(board):
    # Prints the Sudoku board in a neat format.

    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - - ")  # Separator line between 3x3 boxes

        for c in range(9):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")  # Column separator between 3x3 boxes

            if c == 8:
                print(board[r][c])
            else:
                print(str(board[r][c]) + " ", end="")

# --- Example Sudoku Board ---
# 0 represents empty cells
"You can replace this with any Sudoku puzzle you want to solve."
example_board = [
    [5,4,7,0,0,0,8,0,6],
    [0,0,0,7,6,0,0,0,0],
    [0,3,8,2,4,5,0,9,7],
    [0,2,0,4,1,0,9,6,0],
    [0,0,0,9,5,6,0,0,0],
    [7,6,0,0,0,0,0,4,0],
    [0,7,6,0,0,0,4,0,2],
    [8,9,4,1,7,0,6,3,0],
    [0,5,0,6,8,0,7,1,9]
]

# --- Run the Sudoku Solver ---
print("Initial Sudoku Board:")
print_board(example_board)

if solve_sudoku(example_board):
    print("\nFinal Solution Found:")
    print_board(example_board)
else:
    print("\n\nCould not find a solution for this Sudoku.")