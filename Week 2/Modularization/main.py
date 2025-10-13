# main.py
import calculator_utils  # importing your helper file

print("=== Simple Modular Calculator ===")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operation (+, -, *, /): ")

    if operator == "+":
        result = calculator_utils.add(num1, num2)
    elif operator == "-":
        result = calculator_utils.subtract(num1, num2)
    elif operator == "*":
        result = calculator_utils.multiply(num1, num2)
    elif operator == "/":
        result = calculator_utils.divide(num1, num2)
    else:
        result = "Invalid operator!"

    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers!")
