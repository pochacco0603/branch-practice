def fibonacci_iterative(n):
    """Generates the first n Fibonacci numbers iteratively."""
    a, b = 0, 1
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [a, b]
        for _ in range(2, n):
            next_fib = a + b
            sequence.append(next_fib)
            a, b = b, next_fib
        return sequence

# Example usage:
num_terms = 10
fib_sequence = fibonacci_iterative(num_terms)
print(f"Fibonacci sequence (first {num_terms} terms): {fib_sequence}")
