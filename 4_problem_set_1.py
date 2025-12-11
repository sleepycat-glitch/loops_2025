
# # **Python Practice Problems (No Code Included)

# **Directions:** Solve each problem by writing your own Python code. Show outputs where required.


# ### **Problem 1: Print Numbers 1 to 10

# Write a program that prints the numbers from **1 to 10**, each on a new line.

for number in range(1,11):
    print(number)

# ### **Problem 2: Sum of Numbers

# Ask the user for a number **n**, then calculate and display the **sum of all numbers from 1 to n**.

n = int(input("Type in a number: "))
sum = 0
for number in range(1,n+1):
    sum+=number
print(sum)

# ### **Problem 3: Factorial Calculator

# Ask the user for a number **n**, then calculate the **factorial** of that number.

# *(Example: factorial of 5 is 120)


## another method to print factorials using a function:

# def factorial(n):
#     factorial=1
#     for i in range(n):
#         factorial*=i+1

#     return factorial

# print(factorial(10))


n0 = int(input("Type in a number: "))
factorial=1
for num in range(1,n0+1):
    factorial*=num
print(factorial)

# ### **Problem 4: Count Vowels**

# Ask the user for a string. Count and print how many **vowels (a, e, i, o, u)** are in the string.


# ### **Problem 5: Print Even Numbers**

# Ask the user for a number **n**, then print all **even numbers** from 2 up to n.
n1 = int(input("Type in a number: "))
for num in range(0,n1+1):
    if num%2==0:
        print(num)
    else:
        continue


# ### **Problem 6: Reverse a String**

# Ask the user for a string, then print the string **backwards**.

string = input("Type in a word/phrase: ")
print(string[::-1]) #reverse with slicing


# ### **Problem 7: Multiplication Table**

# Ask the user for a number **n**, then print the **multiplication table** for n from
# n × 1 up to n × 10.

n2 = int(input("Type in a number: "))
for num in range(1,11):
    print(f"{n2} x {num} =", n2*num)

# ### **Problem 8: Count Occurrences**

# Ask the user for **two strings**, a and b.
# Determine how many times **string b appears inside string a**.



# ### **Problem 9: Fibonacci Sequence**

# Ask the user for a number **n**, then print the first **n numbers** of the Fibonacci sequence.

# recursion means function calls itself
# ex. fibonacci sequence
def carprice(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return carprice(n-1) + carprice(n-2) 

# calling function within function -> recursion    
print(carprice(6)) # prints 8 

# another method to create fibonacci sequence
def fibonacci(n):
    if n in [1,2]:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,10):
    print(fibonacci(i))


# ### **Problem 10: Pattern Printing**

# Ask the user for a number **n**, then print a pattern of stars where the first row has 1 star, the second has 2, and so on until row n.

# *(Example for n = 4)*
# *
# **
# ***
# ****



# If you want, I can also turn this into a **Google Doc**, **worksheet**, **PDF**, or **Canvas/Schoology assignment format**.
