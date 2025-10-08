N = 8
def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == "Q": return False
        if col-(row-i) >= 0 and board[i][col-(row-i)] == "Q": return False
        if col+(row-i) < N and board[i][col+(row-i)] == "Q": return False
    return True
def solve(board, row=0):
    if row == N:
        for r in board: print(" ".join(r))
        print()
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            if solve(board, row+1): return True
            board[row][col] = "."
    return False
board = [["."]*N for _ in range(N)]
solve(board)
