temperature = float(input("Enter temperature: "))
raining = input("Is it raining? ").strip().lower()

if temperature < 20:
    if raining == "yes":
        print("Wear a jacket and carry an umbrella.")
    else:
        print("Wear a jacket.")
else:
    if raining == "yes":
        print("Wear light clothes and carry an umbrella.")
    else:
        print("Wear light clothes.")
