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







