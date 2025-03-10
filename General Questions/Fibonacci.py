def fibonacci_series(n):
    # initialize the first two terms
    fib_series = [0, 1]
    
    # generate the Fibonacci series
    for _ in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series

# Function to print Fibonacci series up to n terms
def print_fibonacci(n):
    fib_series = fibonacci_series(n)
    print(f"Fibonacci Series up to {n} terms:")
    for num in fib_series:
        print(num, end=" ")

# Taking input from the user for the number of terms
num_terms = int(input("\nEnter the number of terms: "))

# Printing Fibonacci series
print_fibonacci(num_terms)

# Example of fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 89


"""<--------------------------------------------------------------------------->"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("\nEnter number of terms: "))
print("Fibonacci Series:", [fibonacci(i) for i in range(num)])
