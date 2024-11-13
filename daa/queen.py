N = 8

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[0][0] = 1
    print("Board with the first queen placed at (0,0):")
    printSolution(board)
    if not solveNQUtil(board, 1):
        print("Solution does not exist")
        return False
    print("Final solution with all queens placed:")
    printSolution(board)
    return True

if __name__ == '__main__':
    solveNQ()
