DAY 08 - LISTS & TUPLES

1. LIST

A list is an ordered, mutable collection used to store multiple values.

Syntax:
[]

Example:
numbers = [10, 20, 30]
names = ["Ravi", "Teja", "Ankit"]
mixed = [10, "Python", 5.5, True]

List Properties:
- Ordered
- Mutable
- Indexed
- Iterable
- Duplicates allowed
- Dynamic size
- Can store different data types


2. LIST OPERATIONS

1.Concatenation (+):
a = [1, 2]
b = [3, 4]
print(a + b)

Output:
[1, 2, 3, 4]

2.Repetition (*):
print([1, 2] * 3)

Output:
[1, 2, 1, 2, 1, 2]

3.Indexing:
data = [10, 20, 30, 40]
print(data[0])    # 10
print(data[-1])   # 40

4.Slicing:
data = [10, 20, 30, 40, 50]
print(data[1:4])
# [20, 30, 40]

print(data[::-1])
# [50, 40, 30, 20, 10]

5.Membership:
print(20 in data)
# True

print(100 not in data)
# True


3. BUILT-IN LIST FUNCTIONS

len()     -> Returns length
max()     -> Returns largest element
min()     -> Returns smallest element
sum()     -> Returns sum
sorted()  -> Returns sorted list
list()    -> Converts iterable to list


4. LIST METHODS

1.Adding:
append()  -> Adds one element at end
extend()  -> Adds multiple elements
insert()  -> Inserts element at position

2.Removing:
remove()  -> Removes first occurrence
pop()     -> Removes element using index
clear()   -> Removes all elements
del       -> Deletes element/list

3.Searching:
index()   -> Returns index
count()   -> Counts occurrences

4.Sorting:
sort()    -> Sorts original list
reverse() -> Reverses list
sorted()  -> Returns new sorted list

5.Copying:
copy()    -> Creates a shallow copy


5. NESTED LIST

A list inside another list is called a nested list.

Example:
data = [[1, 2], [3, 4]]

print(data[0])
# [1, 2]

print(data[1][1])
# 4

 TUPLE

A tuple is an ordered, immutable collection used to store multiple values.

Syntax:
()

Example:
numbers = (10, 20, 30)
names = ("Ravi", "Teja", "Ankit")
mixed = (10, "Python", 5.5, True)

Tuple Properties:
- Ordered
- Immutable
- Iterable
- Duplicates allowed
- Can store different data types
- Supports nested objects
- Generally faster than lists


7. CREATING TUPLES

Empty tuple:
t = ()

Single element tuple:
t = (10,)

8. TUPLE OPERATIONS

1.Concatenation:
a = (1, 2)
b = (3, 4)
print(a + b)
# (1, 2, 3, 4)

2.Repetition:
print((1, 2) * 3)
# (1, 2, 1, 2, 1, 2)

3.Indexing:
data = (10, 20, 30, 40)

print(data[0])
# 10

print(data[-1])
# 40

4.Slicing:
data = (10, 20, 30, 40, 50)

print(data[1:4])
# (20, 30, 40)

print(data[::-1])
# (50, 40, 30, 20, 10)

5.Membership:
print(20 in data)
# True

print(100 not in data)
# True


9. BUILT-IN TUPLE FUNCTIONS

len()     -> Returns length
max()     -> Returns largest element
min()     -> Returns smallest element
sum()     -> Returns sum
sorted()  -> Returns sorted list
tuple()   -> Converts iterable to tuple
any()     -> True if at least one value is True
all()     -> True if all values are True


10. TUPLE METHODS

Tuples are immutable, so they have only two main methods:

count() -> Counts occurrences
index() -> Returns first occurrence index

Example:
(1, 2, 2, 3).count(2)
# 2

(10, 20, 30).index(20)
# 1


11. TUPLE PACKING

Storing multiple values into a tuple automatically.

data = 10, 20, 30

print(data)
# (10, 20, 30)


12. TUPLE UNPACKING

Extracting tuple elements into variables.

data = (10, 20, 30)

a, b, c = data

print(a)  # 10
print(b)  # 20
print(c)  # 30


13. NESTED TUPLE

A tuple inside another tuple is called a nested tuple.

data = ((1, 2), (3, 4))

print(data[0])
# (1, 2)

print(data[1][1])
# 4


14. TUPLE IMMUTABILITY

Tuple elements cannot be modified.

data = (10, 20, 30)
data[0] = 100

# TypeError


15. MUTABLE OBJECT INSIDE TUPLE

A tuple is immutable, but mutable objects inside it can be modified.

data = (10, [20, 30], 40)

data[1].append(50)

print(data)
# (10, [20, 30, 50], 40)


16. LIST VS TUPLE

List:
- [ ]
- Mutable
- Add/remove/modify allowed
- More memory
- Slightly slower
- Many methods
- Suitable for frequently changing data

Tuple:
- ( )
- Immutable
- Add/remove/modify not allowed
- Less memory
- Faster
- Only count() and index()
- Suitable for fixed data

Both:
- Ordered
- Indexed
- Iterable
- Allow duplicates
- Support different data types
- Support nested structures