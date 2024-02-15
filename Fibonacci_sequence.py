# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

def fibonacci_generator():
    num1 = 0
    num2 = 1
    while num1 <= 100:
        yield num1
        num1, num2 = num2, num1 + num2


# Create a generator object
result = fibonacci_generator()

# Generate Fibonacci numbers up to the value of 100
fibonacci_numbers = list(result)

print(fibonacci_numbers)
