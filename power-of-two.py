# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:
# 8=> returns true
# 6=> returns false

x = 2
# Check if input is a number and if it's greater than 0
while True:
    num = input("Please input a number: ")
    try:
        num = int(num)
        if num <= 0:
            print("Please input a number above 0.")
        else:
            break
    except ValueError:
        print("Please input a valid number.")


# function to check if the input is a power of 2
def is_Power(num, x):
    while num % x == 0:
        num = num // x
    return num == 1


# use of the function
print(is_Power(num, x))
