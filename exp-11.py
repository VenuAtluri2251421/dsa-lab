def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_n_queens(board, col, n):
    if col == n:
        print_board(board)
        return True
    
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            
            res = solve_n_queens(board, col + 1, n) or res
            
            board[i][col] = '.'
    
    return res

n = int(input("Enter the value of n: "))
board = [['.' for _ in range(n)] for _ in range(n)]
solve_n_queens(board, 0, n)

