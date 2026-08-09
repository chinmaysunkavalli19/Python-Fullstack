sentence = input("Enter sentence: ")
words = sentence.split()
reverse = []

for i in range(len(words) - 1, -1, -1):
    reverse.append(words[i])

print(" ".join(reverse))
