class SudokuBoard():
    def __init__(self, board):
        self.board = board
        
    def get(self, row, col):
        return self.board[row][col]
    
    def set(self, row, col, value):
        self.board[row][col] = value
        
    def print_board(self):
        for i in range(len(self.board)):
            if i == 3 or i == 6:
                print("------+-------+-------")
            for j in range(len(self.board[i])):
                if j == 3 or j == 6:
                    print("|", end=" ")
                print(self.board[i][j], end=" ")
            print()
            
    def fill_pencilmarks(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    self.board[i][j] = [i for i in range(1, 10)]


        