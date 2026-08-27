while True:
    year_input = input("Enter a year (or 'Q' to quit): ")

    if year_input.upper() == 'Q':
        break

    try:
        year = int(year_input)
        if year <= 0:
            print("Year must be greater than zero")
            continue
    except ValueError:
        print("Invalid input")
        continue

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")