ch = input("Enter character: ")

if len(ch) == 1 and ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Neither")
