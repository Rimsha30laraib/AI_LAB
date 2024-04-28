class SudokuSolver:
    def solveSudoku(self, board):
        if not self.is_valid_board(board):
            return False
        return self.solve(board)

    def solve(self, board):
        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return True
        
        row, col = empty_cell
        
        for num in range(1, 10):
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num
                
                if self.solve(board):
                    return True
                
                # Backtrack
                board[row][col] = 0
                
        return False

    def is_valid_board(self, board):
        # Check if the board is completely filled
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return True
        return self.validate_filled_board(board)

    def validate_filled_board(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0 and not self.is_valid_move(board, i, j, board[i][j]):
                    return False
        return True

    def is_valid_move(self, board, row, col, num):
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # Check subgrid
        subgrid_row, subgrid_col = row // 3 * 3, col // 3 * 3
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if board[i][j] == num:
                    return False
        
        return True

    def find_empty_cell(self, board):
        # Find the first empty cell in the Sudoku puzzle
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None
    
    def print_board(self, board):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(board[i][j], end=" ")
            print()

# Example usage:
if __name__ == "__main__":
    sudoku_solver = SudokuSolver()
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
    if sudoku_solver.solveSudoku(board):
        print("Sudoku puzzle solved successfully!")
        sudoku_solver.print_board(board)
    else:
        print("No solution exists for the Sudoku puzzle.")
