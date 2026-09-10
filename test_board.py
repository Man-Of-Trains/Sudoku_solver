from SudokuBoard import SudokuBoard
from SudokuSolver import SudokuSolver

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

sudoku_board = SudokuBoard(board)
sudoku_board.print_board()
sudoku_solver = SudokuSolver()
sudoku_solver.test_solve(sudoku_board)
# sudoku_board.fill_pencilmarks()
# sudoku_board.print_board()
# sudoku_board.check_row(0, 2)
# sudoku_board.check_col(0, 2)
# sudoku_board.print_board()
