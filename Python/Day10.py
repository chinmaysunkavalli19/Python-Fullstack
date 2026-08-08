DAY 10 - CONDITIONAL STATEMENTS


1. CONDITIONAL STATEMENTS

Conditional statements are used to check a condition.

They execute different blocks of code based on whether the condition is True or False.

Types of Conditional Statements:

1. if
2. if-else
3. elif
4. Nested if


2. IF STATEMENT

The if statement executes a block of code only when the condition is True.

Syntax:

if condition:
    statements


Example:

a = 10

if a > 5:
    print("Hello")

print("End")

Output:
Hello
End


Example:

a = 20

if a > 20:
    print("Hello")

print("End")

Output:
End

Here 20 > 20 is False, so Hello is skipped.


Real-Time Example:

balance = 5000

if balance >= 1000:
    print("Transaction Allowed")

print("Thank You")


3. IF-ELSE STATEMENT

The if-else statement checks a condition.

If the condition is True, the if block executes.

Otherwise, the else block executes.

Only one block is executed.

Syntax:

if condition:
    statements
else:
    statements


Example:

stock = 5

if stock > 0:
    print("Product Stock Available")
else:
    print("Product Stock Not Available")

Output:
Product Stock Available


Example:

stock = 0

if stock > 0:
    print("Product Stock Available")
else:
    print("Product Stock Not Available")

Output:
Product Stock Not Available


4. VOTING ELIGIBILITY PROGRAM

Problem:
Check whether a person is eligible to vote.

Logic:

Age >= 18
True -> Eligible
False -> Not Eligible

Program:

age = int(input("Enter Age: "))

if age >= 18:
    print("Eligible for Vote")
else:
    print("Not Eligible")

print("End")


Sample Output:

Enter Age: 20
Eligible for Vote
End


5. EVEN OR ODD PROGRAM

Logic:

Number % 2

Remainder = 0 -> Even
Otherwise -> Odd

Program:

num = int(input("Enter Number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


Example:

Enter Number: 10
Even


Example:

Enter Number: 17
Odd


MODULUS (%) OPERATOR

The % operator returns the remainder after division.

Examples:

10 % 2 = 0
15 % 2 = 1
100 % 5 = 0
17 % 2 = 1

If the remainder is 0, the number is Even.

Otherwise, it is Odd.


6. LARGEST OF TWO NUMBERS

Logic:

a > b
True -> a is largest
False -> b is largest

Program:

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a > b:
    print("a is Largest")
else:
    print("b is Largest")


Sample Output:

Enter First Number: 20
Enter Second Number: 10
a is Largest


Sample Output:

Enter First Number: 10
Enter Second Number: 50
b is Largest


7. IF-ELIF-ELSE STATEMENT

The if-elif-else statement is used when multiple conditions need to be checked.

Python evaluates conditions from top to bottom.

As soon as a condition becomes True, its corresponding block executes and the remaining conditions are skipped.

Syntax:

if condition1:
    statements
elif condition2:
    statements
elif condition3:
    statements
else:
    statements


Example:

stock = 5

if stock > 20:
    print("Stock is fully available")
elif stock > 0:
    print("Limited stock available")
else:
    print("Out of stock")


8. NESTED IF STATEMENT

A Nested if is an if statement placed inside another if or else block.

The inner condition is evaluated only when the outer condition is satisfied.

Nested if statements are useful when multiple levels of validation are required.

Syntax:

if condition1:
    if condition2:
        statements
    else:
        statements
else:
    statements


Example:

stock = 10
premium_member = True

if stock > 0:
    print("Product is available")

    if premium_member:
        print("Priority delivery available")
    else:
        print("Standard delivery available")
else:
    print("Product is out of stock")


9. COMPARISON OPERATORS USED IN CONDITIONS

>   Greater than
<   Less than
>=  Greater than or Equal
<=  Less than or Equal
==  Equal to
!=  Not Equal


Examples:

10 > 5      # True
20 > 20     # False
10 == 10    # True
5 != 5      # False
7 <= 10     # True


