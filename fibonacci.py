def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    # Generate subsequent Fibonacci numbers
    for i in range(2, n):
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    return fibonacci_sequence

# Example usage:
num_terms = 10  # Change this value to generate Fibonacci sequence up to a different number of terms
fibonacci_sequence = generate_fibonacci(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fibonacci_sequence)
