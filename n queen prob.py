def is_valid(board, row, col):
    for r, c in enumerate(board):
        if c == col or r + c == row + col or r - c == row - col:
            return False
    return True

def n_queens(n, board=[], row=0):
    if row == n:
        return [board]
    solutions = []
    for col in range(n):
        if is_valid(board, row, col):
            new_board = board + [col]
            solutions += n_queens(n, new_board, row + 1)
    return solutions

n = int(input("Enter the number of queens: "))
solutions = n_queens(n)

print("All possible solutions:")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for col in solution:
        print(" ".join("Q" if c == col else "-" for c in solution))
    print()
