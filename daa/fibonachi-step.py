# Program to display the Fibonacci sequence up to n-th term and count steps
def fibonacci_sequence(nterms):
    # Initialize first two terms and the step counter
    n1, n2 = 0, 1
    step_count = 0  # Initialize step count
    
    # Check if the number of terms is valid
    if nterms <= 0:
        return "Please enter a positive integer.", step_count
    # If there is only one term, return n1
    elif nterms == 1:
        return [n1], 1  # 1 step to print the single term
    
    # Generate Fibonacci sequence
    else:
        sequence = []
        for count in range(nterms):
            sequence.append(n1)
            nth = n1 + n2
            # Update values
            n1 = n2
            n2 = nth
            step_count += 1  # Each iteration counts as 1 step
        return sequence, step_count

# Driver code
if __name__ == "__main__":
    try:
        # Get user input
        nterms = int(input("How many terms? "))
        
        # Call the function to generate Fibonacci sequence
        sequence, steps = fibonacci_sequence(nterms)
        
        # Display results
        if isinstance(sequence, str):
            # Error message if invalid input
            print(sequence)
        else:
            # Print the Fibonacci sequence
            print("Fibonacci sequence up to", nterms, "terms:")
            print(" ".join(map(str, sequence)))
            # Display the total number of steps taken
            print(f"Total number of steps taken: {steps}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
