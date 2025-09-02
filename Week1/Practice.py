# 1. Variables & Data Types
# 👉 Write a program that stores your: Name (string), Age (int) and Height (float)
# Then print them out in a single sentence using string concatenation and f-strings

#My Solution:
# Name = input("Enter your name: ")
# Age = int(input("Enter your age: "))
# Height = float(input("Enter your height in metres: "))
#
# print(f"My name is {Name}, I am {Age} years old and {Height} metres tall!")

# 2. Operators
# 👉 Write a program that:
# Takes two numbers as input.
# Prints their sum, difference, product, quotient, and modulus.
# Uses comparison operators (>, <, ==) to compare them.

#My Solution:
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
#
# sum = x + y
# print(sum)
#
# difference = x - y
# print(difference)
#
# product = x * y
# print(product)
#
# mod = x % y
# print(mod)
#
# if x == y:
#     print("These numbers are equal")
# elif x > y:
#     print("The first number is greater than the second!")
# else:
#     print("The second number is greater than the first!")

# 3. Conditionals (if/else)
# 👉 Write a program that:
# Asks the user for a number.
# Prints whether it is positive, negative, or zero.
# Then check if the number is even or odd.

#My Solution:
# x = int(input("Enter number: "))
#
# if x > 0:
#     sign = "positive"
# elif x < 0:
#     sign = "negative"
# else:
#     print("Your number is zero!")
#
# if (x % 2) == 0:
#     parity = "even"
# else:
#     parity = "odd"
#
# print(f"{x} is {sign} and {parity}")

# 4. Loops
# 👉 Write a program that:
# Prints all numbers from 1 to 20 using a for loop.
# Prints all even numbers between 1 and 50 using a while loop.

#My Solution:
# For loop: numbers 1–20
for x in range (1,21):
    print(x)

# While loop: even numbers 0–50
i = 0
while i < 51:
    if i % 2 == 0:
        print(i)
    i+=1
