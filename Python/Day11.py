DAY 11 - LOOPS

 LOOPS

A loop is used to execute a block of code repeatedly.

Without a loop:

print(1)
print(2)
print(3)
print(4)
print(5)

Using a loop:

for i in range(1, 6):
    print(i)

Output:

1
2
3
4
5


Advantages of Loops:

- Reduces code repetition
- Saves development time
- Makes code shorter
- Improves code readability
- Makes repetitive tasks easier to automate


8. TYPES OF LOOPS IN PYTHON

1. for loop
2. while loop

1. FOR LOOP

The for loop is used to iterate over a sequence or iterable.

Examples of iterables:

- list
- tuple
- string
- set
- dictionary
- range

Syntax:

for variable in iterable:
    statements


Example:

numbers = [10, 20, 30, 40]

for i in numbers:
    print(i)

Output:

10
20
30
40


1. ITER() FUNCTION

The iter() function is used to obtain an iterator from an iterable.

Example:

l = [1, 2, 3, 4]

i = iter(l)

print(i)


2. NEXT() FUNCTION

The next() function gets the next value from an iterator.

Example:

l = [1, 2, 3, 4]

i = iter(l)

print(next(i))
print(next(i))
print(next(i))
print(next(i))

Output:

1
2
3
4

Every time next(i) is called, the iterator moves forward.


3. STOPITERATION

After the last element, if next() is called again, Python raises StopIteration.

Example:

l = [1, 2, 3, 4]

i = iter(l)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

The fifth call raises:

StopIteration

The for loop automatically handles StopIteration internally.


5. RANGE() FUNCTION

range() is used to generate a sequence of numbers.

Syntax:

range(start, stop, step)

Parameters:

start = Starting value
stop = Ending boundary
step = Difference between values

Important:

The stop value is NOT included.


6. RANGE(1, 10)

r = range(1, 10)

l = list(r)

print(l)

Output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

10 is not included.


7. RANGE(10)

If only one argument is provided:

range(10)

Python assumes:

start = 0
stop = 10
step = 1

Example:

r = range(10)

print(list(r))

Output:

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


16. RANGE() AND ITER()

Example:

r = range(10)

i = iter(r)

print(next(i))
print(next(i))
print(next(i))

Output:

0
1
2


* RANGE() VS ITER()

range()
→ Creates a range object.

iter()
→ Creates an iterator from an iterable.

next()
→ Gets the next value from the iterator.

Flow:

range()
↓
range object
↓
iter()
↓
iterator
↓
next()
↓
next value


18. FOR LOOP WITH RANGE()

Example:

for i in range(1, 6):
    print(i)

Output:

1
2
3
4
5


. REVERSE LOOP

We can use a negative step to move backward.

Example:

for i in range(10, 0, -1):
    print(i)

Output:

10
9
8
7
6
5
4
3
2
1

Here:

start = 10
stop = 0
step = -1

0 is excluded.


20. DIFFERENT RANGE() EXAMPLES

range(1, 6)

Values:

1 2 3 4 5


range(1, 11, 2)

Values:

1 3 5 7 9


range(1, 20, 3)

Values:

1 4 7 10 13 16 19


range(10, 0, -1)

Values:

10 9 8 7 6 5 4 3 2 1


Ex: PRINTING EVEN NUMBERS

An even number is divisible by 2.

Condition:

i % 2 == 0

Program:

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

Output:

2
4
6
8
10


. IF INSIDE A FOR LOOP

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

Here:

for controls repetition.

if controls selection.

Logic:

for each number
↓
check whether it is even
↓
if True → print
if False → skip


23. IMPORTANT CONCEPT FLOW

CONDITIONAL STATEMENTS

if
↓
if-else
↓
if-elif-else
↓
nested if

LOOPS

for loop
↓
while loop

FOR LOOP

Iterable
↓
iter()
↓
Iterator
↓
next()
↓
Next value
↓
Repeat until StopIteration



