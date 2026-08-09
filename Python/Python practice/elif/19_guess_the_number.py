import random

number = random.randint(1, 10)
guess = int(input("Guess the number: "))

if guess == number:
    print("Congratulations! You guessed the number.")
else:
    print("Wrong guess. Try again.")
    print("The number was:", number)
