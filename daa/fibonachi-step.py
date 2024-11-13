def fibonacci(n):
    a = 0
    b = 1
    step_count = 0
    series = []
    for _ in range(n):
        series.append(a)
        step_count += 1
        a, b = b, a + b
    return series, step_count

n = int(input("enter the number for fibonacci : "))
fib_series, steps = fibonacci(n)
print(f"Fibonacci series up to {n} terms: {fib_series}")
print(f"Number of steps taken: {steps}")
