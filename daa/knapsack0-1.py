# Function to solve the 0-1 Knapsack problem using dynamic programming
def knapSack(W, wt, val, n):
    # Create a 2D array to store the maximum value that can be obtained
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            # Base Case: If no items or weight is 0, value is 0
            if i == 0 or w == 0:
                K[i][w] = 0
            # If weight of the ith item is less than or equal to current capacity
            elif wt[i - 1] <= w:
                # Take the maximum of including or excluding the item
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                # If the item cannot be included, carry forward the previous value
                K[i][w] = K[i - 1][w]

    # The maximum value is found in K[n][W]
    return K[n][W]

# Driver Code
if __name__ == '__main__':
    try:
        # Get the number of items from the user
        n = int(input("Enter the number of items: "))

        # Get profit and weight of each item
        profit = []
        weight = []

        for i in range(n):
            val = int(input(f"Enter profit for item {i+1}: "))
            wt = int(input(f"Enter weight for item {i+1}: "))
            profit.append(val)
            weight.append(wt)

        # Get the knapsack capacity
        W = int(input("Enter the capacity of the knapsack: "))

        # Function call
        max_profit = knapSack(W, weight, profit, n)
        print("Maximum profit:", max_profit)

    except ValueError:
        print("Invalid input. Please enter valid numbers for profits, weights, and capacity.")
