class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda item: item.value/item.weight, reverse=True)

    total_value = 0
    for item in items:
        if capacity == 0:
            break
        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0
    
    return total_value

if __name__ == "__main__":
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50

    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in the knapsack: {max_value}")


