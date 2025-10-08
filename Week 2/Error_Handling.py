try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("You can’t divide by zero.")
else:
    print("Result:", result)        # runs only if no exception
finally:
    print("Done.")               # always runs
