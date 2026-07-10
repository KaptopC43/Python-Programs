def bmi_func(weight, height):
    return weight / (height**2)


while True:
    weight_input = input("Enter weight in kg (or 'Q' to quit): ").strip().upper()

    if weight_input == "Q":
        print("Closing program")
        break

    try:
        weight = float(weight_input)
    except ValueError:
        print("Invalid input")
        continue

    if weight <= 0:
        print("Invalid input: Weight and height must be greater than 0")
        continue

    while True:
        height_input = input("Enter height in m: ").strip().upper()
        try:
            height = float(height_input)
            if height > 0:
                break
            else:
                print("Invalid input: Weight and height must be greater than 0")
        except ValueError:
            print("Invalid input")

    bmi = bmi_func(weight, height)
    print(f"BMI is {bmi:.1f}")

    if bmi < 18.5:
        print("You are underweight")
    elif bmi < 25:
        print("You are normal")
    elif bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")