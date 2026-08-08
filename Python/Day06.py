DAY 06 - INPUT & OUTPUT FORMATTING

1. INPUT FORMATTING

input() is used to take input from the user.
By default, input() returns a string.

String Input:
name = input("Enter your name: ")

Integer Input:
age = int(input("Enter your age: "))

Float Input:
price = float(input("Enter price: "))

List Input - Space Separated:
names = input("Enter names: ").split()

List Input - Comma Separated:
tags = input("Enter tags: ").split(",")

List of Integers:
marks = list(map(int, input("Enter marks: ").split()))

List of Floats:
weights = list(map(float, input("Enter weights: ").split()))

Tuple Input:
dimensions = tuple(map(int, input("Enter values: ").split()))

Set Input:
ids = set(map(int, input("Enter IDs: ").split()))

Dictionary Input:
profile = eval(input("Enter profile: "))

Multiple Inputs:
username, password = input("Enter username and password: ").split()


2. OUTPUT FORMATTING

print() is used to display data on the screen.

Syntax:
print(object, sep=' ', end='\n')

sep:
Used to specify the separator between multiple values.

Example:
print("2005", "09", "19", sep="-")

Output:
2005-09-19

end:
Used to control what comes at the end of print().

Example:
print("Hello", end=" ")
print("World")

Output:
Hello World


3. SPECIAL CHARACTERS

New Line:
\n

Example:
print("Line 1\nLine 2")

Tab:
\t

Example:
print("Name:\tAlice")


4. OUTPUT FORMATTING METHODS

1. Comma Method

name = "Alice"
age = 25
print("Name:", name, "Age:", age)


2. Modulo (%) Formatting

name = "Bob"
age = 30
score = 88.75

print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))

%s -> String
%d -> Integer
%f -> Float


3. f-Strings

Modern and recommended method.

name = "Charlie"
age = 28
score = 92.389

print(f"Name: {name} | Age: {age} | Score: {score:.2f}")

:.2f -> 2 decimal places


4. str.format()

name = "Diana"
age = 22
score = 89.456

print("Name: {} | Age: {} | Score: {:.1f}".format(name, age, score))

{ } -> Placeholder
{:.1f} -> 1 decimal place


IMPORTANT:
f-strings are available from Python 3.6+.