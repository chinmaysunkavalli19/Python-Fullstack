DAY 07 - STRINGS

1. STRING

A string is a sequence of characters enclosed within:
' '  → Single quotes
" "  → Double quotes
''' ''' or """ """ → Triple quotes

Strings are immutable.
Once a string is created, it cannot be changed.

Example:
str1 = 'Hello'
str2 = "World"
str3 = '''This is a multi-line
string example.'''


2. STRING OPERATIONS

1. Concatenation (+)
Joining two or more strings.

str1 = "Hello"
str2 = "World"

result = str1 + " " + str2
print(result)

Output:
Hello World


2. Repetition (*)
Repeating a string multiple times.

print("Python! " * 3)

Output:
Python! Python! Python!


3. Indexing
Accessing individual characters using index.

text = "Python"

print(text[0])
Output: P

print(text[-1])
Output: n


4. Slicing
Extracting a part of a string.

text = "Python"

print(text[0:3])
Output: Pyt

print(text[:4])
Output: Pyth

print(text[2:])
Output: thon


5. Membership

'in' → Checks whether substring exists.
'not in' → Checks whether substring does not exist.

print("Pyt" in "Python")
Output: True

print("Java" not in "Python")
Output: True


3. BUILT-IN STRING FUNCTIONS

1.len():Returns length of string.
Example:
text = "Hello World"
print(len(text))

Output:
11

2.max():Returns character with highest ASCII value.
Example:
print(max("abcXYZ"))

Output:
c


3.min():Returns character with lowest ASCII value.
Example:
print(min("abcXYZ"))

Output:
X


4.sorted():Returns sorted list of characters.
Example:
print(sorted("python"))

Output:
['h', 'n', 'o', 'p', 't', 'y']


5.ord():Converts character into ASCII value.
Example:
print(ord('A'))

Output:
65

6.chr():Converts ASCII value into character.
Example:
print(chr(97))

Output:
a


4. CASE CONVERSION METHODS

1.upper():Converts all characters to uppercase.
Example:
"hello".upper()
→ "HELLO"


2.lower():Converts all characters to lowercase.
Example:
"HELLO".lower()
→ "hello"


3.capitalize():Capitalizes the first character.
Example:
"python".capitalize()
→ "Python"

4.title():Capitalizes the first letter of each word.
Example:
"hello world".title()
→ "Hello World"


5.swapcase():Converts uppercase to lowercase and lowercase to uppercase.
Example:
"PyThOn".swapcase()
→ "pYtHoN"

6.casefold():Converts string to lowercase.
It is more aggressive than lower().
example:
"HELLO".casefold()
→ "hello"


5. ALIGNMENT & FORMATTING METHODS

1.center():Centers the string within given width.
Example:
"python".center(10, "*")
→ "**python**"


2.ljust():Left-aligns the string.
Example:
"py".ljust(5, "-")
→ "py---"


3.rjust():Right-aligns the string.
Example:
"py".rjust(5, "-")
→ "---py"

4.zfill():Adds zeros to the left.
Example:
"42".zfill(5)
→ "00042"

6. SEARCH & FIND METHODS

1.find():Returns index of first occurrence.Returns -1 if not found.
Example:
"hello".find("l")
→ 2

2.rfind():Returns index of last occurrence.
Example:
"hello".rfind("l")
→ 3

3.index():Same as find(), but raises an error if substring is not found.
Example:
"hello".index("e")
→ 1


4.rindex():Same as rfind(), but raises an error if substring is not found.
Example:
"hello".rindex("l")
→ 3

5.count():Counts how many times a substring occurs.
Example:
"banana".count("a")
→ 3


7. STRING TESTING METHODS

These methods return Boolean values:
True or False.


1.startswith():Checks whether string starts with given substring.
Example:
"python".startswith("py")
→ True


2.endswith():Checks whether string ends with given substring.
Example:
"python".endswith("on")
→ True

3.isalpha():Returns True if all characters are alphabets.
Example:
"Hello".isalpha()
→ True

4.isalnum():Returns True if all characters are alphabets or numbers.
Example:
"abc123".isalnum()
→ True

5.islower():Checks whether all characters are lowercase.
Example:
"hello".islower()
→ True

6.isupper():Checks whether all characters are uppercase.
Example:
"HELLO".isupper()
→ True

7.isspace():Checks whether all characters are whitespace.
Example:
" ".isspace()
→ True

8.istitle():Checks whether string is in title case.
Example:
"Hello World".istitle()
→ True

9.isidentifier():Checks whether string is a valid Python identifier.
Example:
"variable1".isidentifier()
→ True

8. isdecimal(), isdigit(), isnumeric()

1.isdecimal()
Most strict.
Checks base-10 decimal digits.

2.isdigit()
Allows additional digit characters like superscripts.

3.isnumeric()
Most flexible.
Includes digits, fractions and Roman numerals.

Example:

"123".isdecimal()
→ True

"²".isdigit()
→ True

"⅓".isnumeric()
→ True


9. REPLACE & MODIFY METHODS

1.replace():Replaces old substring with new substring.
Example:
"apple".replace("p", "b")
→ "abble"


2.translate():Replaces characters using a translation table.
Example:
"abc".translate(str.maketrans("a", "x"))
→ "xbc"

2.maketrans():Creates a translation table for translate().


10. SPLITTING & JOINING METHODS

1.split():Splits string into a list.
Example:
"a,b,c".split(",")
→ ['a', 'b', 'c']


2.rsplit():Splits from the right side.
Example:
"a,b,c".rsplit(",", 1)
→ ['a,b', 'c']


3.splitlines():Splits string at line breaks.
Example:
"Hello\nWorld".splitlines()
→ ['Hello', 'World']


4.join():Joins elements using a separator.
Example:
" ".join(["Hello", "World"])
→ "Hello World"

5.partition():Splits string into a 3-part tuple at the first separator.
Example:
"apple-pie".partition("-")
→ ('apple', '-', 'pie')


6.rpartition():Splits into a 3-part tuple at the last separator.
Example:
"apple-pie".rpartition("-")
→ ('apple', '-', 'pie')


11. WHITESPACE & TRIMMING METHODS

1.strip():Removes leading and trailing characters.Default is spaces.
Example:
" hello ".strip()
→ "hello"


2.lstrip():Removes characters from the left side.
Example:
"---hello".lstrip("-")
→ "hello"

3.rstrip():Removes characters from the right side.
Example:
"hello---".rstrip("-")
→ "hello"


12. ENCODING & DECODING

1.encode():Converts string into bytes.
Example:
"hello".encode("utf-8")
→ b'hello'

2.decode():Converts bytes back into string.
Example:
b'hello'.decode("utf-8")
→ "hello"