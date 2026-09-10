class SudokuSolver():
    def __init__(self):
        pass
    
    def test_solve(self, board):
        self.board = board
        self.board.fill_pencilmarks()
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                if isinstance(self.board.board[i][j], list):
                    self.board.check_row(i, j)
                    self.board.check_col(i, j)
        self.board.print_board()
                    
    def check_row(self, row, col):
            for j in range(len(self.board[row])):
                if isinstance(self.board[row][j], list):
                    continue
                else:
                    if self.board[row][j] in self.board[row][col]:
                        print("Value removed!")
                        self.board[row][col].remove(self.board[row][j])
                        
    def check_col(self, row, col):
        for i in range(len(self.board)):
            if isinstance(self.board[i][col], list):
                continue
            else:
                if self.board[i][col] in self.board[row][col]:
                    print("Value removed!")
                    self.board[row][col].remove(self.board[i][col])
    