class SudokuSolver():
    def __init__(self):
        pass
    
    def test_solve(self, board):
        self.board = board
        self.board.fill_pencilmarks()
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                if isinstance(self.board.board[i][j], list):
                    self.check_row(self.board.board, i, j)
                    self.check_col(self.board.board, i, j)
                    self.check_box(self.board.board, i, j)
        self.board.print_board()
                    
    def check_row(self, board, row, col):
            for j in range(len(board[row])):
                if isinstance(board[row][j], list):
                    continue
                else:
                    if board[row][j] in board[row][col]:
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[row][j]}")
                        board[row][col].remove(board[row][j])
                        
    def check_col(self, board, row, col):
        for i in range(len(board)):
            if isinstance(board[i][col], list):
                continue
            else:
                if board[i][col] in board[row][col]:
                    print(f"Value removed! row {row+1}, col {col+1}, num {board[i][col]}")
                    board[row][col].remove(board[i][col])
                    
    def check_box(self, board, row, col):
        # Check box 1
        if row <= 2 and col <= 2:
            for i in range(0,3):
                for j in range(0,3):
                    if board[i, j] in board[row][col] and (i != row and j != col):
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")
        # Check box 2
        elif row <= 2 and (col > 2 and col <= 5):
            for i in range(0,3):
                for j in range(3,6):
                    if board[i, j] in board[row][col] and (i != row and j != col):
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")
        # Check box 3
        elif row <= 2 and col > 5:  
            for i in range(0,3):
                for j in range(6,9):
                    if board[i, j] in board[row][col] and (i != row and j != col):
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")
        # Check box 4
        elif (row > 2 and row <= 5) and col <= 2:
            for i in range(3,6):
                for j in range(0,3):
                    if board[i, j] in board[row][col] and (i != row and j != col):
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")        
        # Check box 5
        elif (row > 2 and row <= 5) and (col > 2 and col <= 5):
            for i in range(3,6):
                if board[i, j] in board[row][col] and (i != row and j != col):
                    print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")      
        # Check box 6
        elif (row > 2 and row <= 5) and col > 5: 
            for i in range(3,6):
                for j in range(6,9):
                    if board[i, j] in board[row][col] and (i != row and j != col):
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")
        # Check box 7
        elif row > 5 and col <= 2:
            for i in range(6,9):
                for j in range(0,3):
                    if board[i, j] in board[row][col] and (i != row and j != col):
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")
        # Check box 8
        elif row > 5 and (col > 2 and col <= 5):
            for i in range(6,9):
                for j in range(3,6):
                    if board[i, j] in board[row][col] and (i != row and j != col):
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")
        # Check box 9
        elif row > 5 and col > 5: 
            for i in range(6,9):
                for j in range(6,9):
                    if board[i, j] in board[row][col] and (i != row and j != col):
                        print(f"Value removed! row {row+1}, col {col+1}, num {board[i][j]}")