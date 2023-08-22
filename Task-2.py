def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the first two Fibonacci numbers
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_numbers = fibonacci(n)
print("Fibonacci sequence:", fib_numbers)
