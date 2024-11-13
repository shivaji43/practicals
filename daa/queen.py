N = 8  # Set board size for 8-queens problem

def printSolution(board):
    """Prints the chessboard with queens placed."""
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()  # Newline for better readability

def isSafe(board, row, col):
    """Check if a queen can be placed at board[row][col]."""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    """Utilizes backtracking to place queens in each column."""
    # Base case: If all queens are placed
    if col >= N:
        return True

    # Try placing the queen in each row in the current column
    for i in range(N):
        if isSafe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            # If placing queen doesn't lead to a solution, remove it (backtrack)
            board[i][col] = 0

    return False

def solveNQ():
    """Initializes the board and solves the 8-queens problem."""
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Place the first queen manually for visualization
    board[0][0] = 1  # First queen placed in top-left corner
    print("Board with the first queen placed at (0,0):")
    printSolution(board)

    # Solve for the remaining queens
    if not solveNQUtil(board, 1):  # Start from the second column
        print("Solution does not exist")
        return False

    # Print the final solution
    print("Final solution with all queens placed:")
    printSolution(board)
    return True

# Driver code
if __name__ == '__main__':
    solveNQ()
