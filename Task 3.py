# Job Eligibility Checker

age = int(input("Enter your age: "))
qualification = input("Enter your qualification (e.g., graduate): ").lower()

if age >= 21:
    if qualification == "graduate":
        print("You are eligible for the job.")
    else:
        print("Qualification not sufficient.")
else:
    print("Not eligible due to age.")
