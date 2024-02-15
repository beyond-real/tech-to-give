# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19

# Check if input is a number
while True:
    num = input("Please input a number: ")
    try:
        num = int(num)
        break
    except ValueError:
        print("Please input a valid number.")


def reverse_number(num):
    # Handle negative numbers
    is_negative = num < 0
    if is_negative:
        num = abs(num)  # Make the number positive temporarily

    reversed_num = 0

    # Iterate until the original number becomes 0
    while num != 0:
        # Extract the last digit from the original number
        digit = num % 10

        # Make the reversed number
        reversed_num = reversed_num * 10 + digit

        # Get the last first digit from the original number
        num //= 10

    # Change negative to positive
    if is_negative:
        reversed_num *= -1

    return reversed_num


# Function use
number = num
reversed_number = reverse_number(number)
print("Original number:", number)
print("Reversed number:", reversed_number)
