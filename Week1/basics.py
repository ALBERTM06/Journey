# Assigning variables
x = 10             # integer
y = 3.14           # float
name = "Albert"    # string
is_coding = True   # boolean

# Multiple assignment
a, b, c = 1, 2, 3

# Checking types
print(type(x))     # <class 'int'>

# Numbers
x = 5 + 3       # addition → 8
y = 10 - 4      # subtraction → 6
z = 2 * 6       # multiplication → 12
w = 7 / 2       # division → 3.5
v = 7 // 2      # floor division → 3
m = 7 % 2       # modulus → 1
p = 2 ** 3      # exponent → 8

# Strings(Note: Strings are arrays)
s = "Hello"
print(s.upper())      # "HELLO"
print(s.lower())      # "hello"
print(s[0])           # indexing → 'H'
print(s[0:3])         # slicing → "Hel"
print(len(s))         # length → 5

for i in "banana":   #Looping through a string
    print(i)

friendzone = "I love you as a friend!" #More fun with the in keyword and if loop
if "love" in friendzone:
    print("So far so good")
if "friend" in friendzone:
    print("That's rough buddy :(")

age = int(input("Enter your age: "))   #User input, boolean variable, conditionals and typecasting
is_human = True
print(age)
if is_human == True:
    print("Greetings human!")
else:
    print("Sorry bud! Humans only!")

if age>=18:
    print("Welcome to adult life! Pay your taxes!")
elif age< 0:
    print("You are yet to be born young one!")
elif age>=65:
    print("Enjoy your retirement, you deserve it!")
elif age == 0:
    print("Welcome to the world!")
else:
    print("Enjoy your childhood while it still lasts >:(")

# Lists
fruits = ["apple", "banana", "cherry"]

# Accessing
print(fruits[0])      # "apple"
print(fruits[-1])     # "cherry" (negative index counts from end)

# Slicing
print(fruits[0:2])    # ["apple", "banana"]

# Modifying
fruits[1] = "mango"
print(fruits)         # ["apple", "mango", "cherry"]

# Adding
fruits.append("orange")
print(fruits)         # ["apple", "mango", "cherry", "orange"]

# Removing
fruits.remove("apple")
print(fruits)         # ["mango", "cherry", "orange"]

# Looping
for f in fruits:
    print(f)

# Sorting
fruits.sort()
print(fruits)         # ["cherry", "mango", "orange"]

#Tuples
coordinates = (10.0, 20.5, 30.2)

print(coordinates[0])    # 10.0
print(len(coordinates))  # 3

# coordinates[0] = 15.0   ❌ ERROR → cannot modify tuples

# Tuple unpacking
x, y, z = coordinates
print(x, y, z)   # 10.0 20.5 30.2

#Sets
numbers = {1, 2, 3, 3, 4, 5}
print(numbers)      # {1, 2, 3, 4, 5} (duplicates removed)

# Adding elements
numbers.add(6)
print(numbers)

# Removing
numbers.remove(2)
print(numbers)

# Membership test
print(3 in numbers)    # True

# Set operations
evens = {2, 4, 6, 8}
print(numbers.union(evens))        # combine sets
print(numbers.intersection(evens)) # common elements

#Dictionaries
student = {
    "name": "Albert",
    "age": 20,
    "major": "Computer Science"
}

# Access
print(student["name"])    # Albert
print(student.get("age")) # 20

# Modify
student["age"] = 21

# Add new key
student["gpa"] = 3.8

# Remove key
student.pop("major")

# Looping
for key, value in student.items():
    print(key, ":", value)

#Functions
# Simple function
def greet(name):
    print("Hello, " + name + "!")

greet("Albert")    # Hello, Albert!

# Function with return
def add(x, y):
    return x + y

print(add(5, 3))   # 8

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # 9 (3^2)
print(power(2, 3))    # 8 (2^3)

# Scope
x = 10
def change():
    x = 5   # local variable
    print("Inside:", x)

change()           # Inside: 5
print("Outside:", x)  # Outside: 10










