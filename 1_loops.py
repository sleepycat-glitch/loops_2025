# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
#abstracted version of previous code
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)

# print out each subject but stops when reach "History"
for subject in subjects:
    if subject=="History":
        break
    else:
        print(subject)

# prints out each subject but skips over "Science"
for subject in subjects:
    if subject=="Science":
        continue
    else:
        print(subject)
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for i in range(len(subjects)):
    print(f"Subject {i}: {subjects[i]}")


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
# set base variable
# += adds current value to previous value
total = 0
for number in numbers:
    total+=number
print(total)
    