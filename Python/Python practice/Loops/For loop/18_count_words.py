sentence = input("Enter sentence: ")
count = 0

for word in sentence.split():
    count += 1

print("Number of words:", count)
