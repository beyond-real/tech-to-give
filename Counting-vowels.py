# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2


vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]   # initializing a list of vowels
total_vowel_count = 0
encountered_vowels = []

sentence = input("Write a sentence: ")   # input
words = sentence.split()    # splitting the sentence to words

# check for vowels in the words
for word in words:
    for char in word:
        if char in vowels and char.lower() not in encountered_vowels:
            encountered_vowels.append(char.lower())
            total_vowel_count += 1

print("The vowels are: ", encountered_vowels)
print("The number of vowels is:", total_vowel_count)
