choice = input("Enter conversion: ").strip().lower()
temperature = float(input("Enter temperature: "))

if choice == "c to f":
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == "f to c":
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid conversion")
