# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.
word = input("Type in a word: ")
for letter in word:
    print(letter)

# Challenge:
# Count how many vowels are in the word.
vowels = "aeiouAEIOU"
counter = 0
word1 = input("Type in a word: ")
for letter in word:
    if letter in vowels:
        counter+=1

print(counter)

