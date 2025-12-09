# notes:
# name = input("Enter your name: ")
# executes code while true, while false, exits loop
# if no brake in while loop, will continue forever
# while name == "":
#     print("You did not enter your name.")
#     name = input("Enter your name: ")
# print(f"Hello {name}.")


# age = int(input("Enter your age: "))

# while age<0:
#     print("Age can't be negative.")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old.")

# foods = [ ]
# # if empty list is inside while loop, then it will erase the list every time it runs
# food = input("Enter a food you like (press q to quit): ")
# while not food == "q":
#     foods.append(food)
#     print(f"You like {food}.")
#     food = input("Enter a food you like (press q to quit): ")
# print(f"You like the following foods: {foods}")
# print("Bye.")


# num = int(input("Enter a number between 1-10: "))
# while num <1 or num>10:
#     print(f"{num} is not valid.")
#     num = int(input("Enter a number between 1-10: "))
# print(f"Your number is {num}.")

    
# # Given:
# colors = ["red", "blue", "green", "yellow", "purple"]

# # Challenge:
# # Use a while loop to print each color UNTIL you find "yellow".
# # Do NOT print "yellow" — stop before it.

# index = 0
# while index<len(colors):
#     if colors[index] == "yellow":
#         break
#     print(colors[index])
#     index+= 1 # increments index to avoid infinite loop

# # for loop version of previous code 
# for color in colors:
#     if color =="yellow":
#         break
#     else:
#         print(color)

