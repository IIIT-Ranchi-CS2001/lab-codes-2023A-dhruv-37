import random
import math
import matplotlib.pyplot as plt

def generate_random_numbers(K, N):
    if K < 10:
        raise ValueError("K must be at least 10.")
    return [random.randint(2, N) for _ in range(K)]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def separate_primes_and_composites(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if not is_prime(num)]
    return primes, composites

def main():
    K = int(input("Enter the number of random numbers (K >= 10): "))
    N = int(input("Enter the limit (N): "))
    
    numbers = generate_random_numbers(K, N)
    
    primes, composites = separate_primes_and_composites(numbers)
    
    prime_squares = [p ** 2 for p in primes]
    composite_roots = [math.sqrt(c) for c in composites]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Primes vs. Squares and Composites vs. Square Roots", fontsize=16)
    
    ax1.scatter(primes, prime_squares, color='blue', edgecolor='black')
    ax1.set_xlabel("Prime Numbers")
    ax1.set_ylabel("Square of Prime Numbers")
    ax1.set_title("Primes vs. Squares")
    
    ax2.scatter(composites, composite_roots, color='green', edgecolor='black')
    ax2.set_xlabel("Composite Numbers")
    ax2.set_ylabel("Square Root of Composite Numbers")
    ax2.set_title("Composites vs. Square Roots")
    
    plt.show()

main()
