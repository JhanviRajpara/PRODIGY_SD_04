def is_valid(board, row, col, num):
    # Check if the number is not in the current row, column, and 3x3 sub-grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):  # Recursively solve the rest
                            return True
                        board[row][col] = 0  # Backtrack if solution not found
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def main():
    # Example unsolved Sudoku puzzle (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku puzzle:")
    print_board(board)
    
    if solve_sudoku(board):
        print("\nSolved Sudoku puzzle:")
        print_board(board)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
