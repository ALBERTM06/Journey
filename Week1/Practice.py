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
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

sum = x + y
print(sum)

difference = x - y
print(difference)

product = x * y
print(product)

mod = x % y
print(mod)

if x == y:
    print("These numbers are equal")
elif x > y:
    print("The first number is greater than the second!")
else:
    print("The second number is greater than the first!")