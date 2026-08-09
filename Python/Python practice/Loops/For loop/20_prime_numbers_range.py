start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
primes = []

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print("Prime numbers:", primes)
