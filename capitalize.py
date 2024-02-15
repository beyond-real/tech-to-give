# #Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "I love programming"=> returns "I Love Programming"

# Accepting input
a = input("Please input a sentence of your liking: ")
count = 0

# splitting string to a list
b = a.split()

# capitalizing the first letter
for i in b:
    b[count] = b[count].capitalize()
    count += 1

# joining the list back to a string
a = " ".join(b)
print("The result is: {}".format(a))
