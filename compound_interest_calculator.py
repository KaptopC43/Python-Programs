def compound_interest(p, r, t):
    return p * ((1 + r/100)**t) - p

running = True

while running:
    principal_input = input("Enter the principal (or 'Q' to quit): ").strip().upper()

    if principal_input == "Q":
        print("Closing program")
        break

    try:
        principal = float(principal_input)
    except ValueError:
        print("Invalid input")
        continue

    if principal <= 0:
        print("Invalid input: Principal must be greater than 0")
        continue

    while running:
        rate_input = input("Enter the rate in percentage (or 'Q' to quit): ").strip().upper()

        if rate_input == "Q":
            print("Closing program")
            running = False
            break

        try:
            rate = float(rate_input)
        except ValueError:
            print("Invalid input")
            continue

        if rate <= 0:
            print("Invalid input: Rate must be greater than 0")
            continue

        while running:
            years_input = input("Enter the number of years (or 'Q' to quit): ").strip().upper()

            if years_input == "Q":
                print("Closing program")
                running = False
                break

            try:
                years = float(years_input)
            except ValueError:
                print("Invalid input")
                continue

            if years <= 0:
                print("Invalid input: Years must be greater than 0")
                continue

            interest = compound_interest(principal, rate, years)
            total_amount = principal + interest

            print(f"Compound interest: {interest:.2f}")
            print(f"Total amount: {total_amount:.2f}")

            break
        break
