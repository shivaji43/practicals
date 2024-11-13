# Class for an Item which stores profit and weight
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Comparison function to sort items based on profit/weight ratio
def cmp(item):
    return item.profit / item.weight

# Main greedy function to solve the Fractional Knapsack problem
def fractional_knapsack(W, items):
    # Sort items by profit-to-weight ratio in descending order
    items.sort(key=cmp, reverse=True)

    final_value = 0.0  # Total profit

    for item in items:
        # If adding the entire item doesn't exceed the capacity, add it fully
        if item.weight <= W:
            W -= item.weight
            final_value += item.profit
        else:
            # Otherwise, add the fractional part of the item
            final_value += item.profit * (W / item.weight)
            break  # Knapsack is full

    return final_value

# Driver code
if __name__ == "__main__":
    try:
        # Get the weight capacity of the knapsack from the user
        W = int(input("Enter the weight capacity of the knapsack: "))

        # Get the number of items from the user
        n = int(input("Enter the number of items: "))

        # List to store items
        items = []

        # Get profit and weight for each item
        for i in range(n):
            profit = float(input(f"Enter profit for item {i+1}: "))
            weight = float(input(f"Enter weight for item {i+1}: "))
            items.append(Item(profit, weight))

        # Function call
        max_profit = fractional_knapsack(W, items)
        print("Maximum profit:", max_profit)

    except ValueError:
        print("Invalid input. Please enter valid numbers for weights and profits.")
