import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_up_to_n(n):
    """Print all prime numbers up to N."""
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    print(f"Prime numbers up to {n} : {primes}")

# Example Usage
num = int(input("\nEnter a number to check if it's prime: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

n = int(input("\nEnter a number to print all primes up to N: "))
print_primes_up_to_n(n)
