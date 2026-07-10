def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


while True:
    user_input = input("Enter temperature (or 'Q' to quit): ").strip().upper()

    if user_input == "Q":
        print("Closing program")
        break

    try:
        temp = float(user_input)
    except ValueError:
        print("Invalid input")
        continue

    while True:
        unit = str(input("Enter unit (C or F): ")).strip().upper()

        if unit == "C":
            temp = celsius_to_fahrenheit(temp)
            output_unit = "F"
            break
        elif unit == "F":
            temp = fahrenheit_to_celsius(temp)
            output_unit = "C"
            break
        else:
            print("Invalid unit")

    print(f"{temp:.1f}°{output_unit.upper()}")