while True:
    try:
        human_age = int(input("Enter the dog's age in human years: "))
        if human_age >= 0:
            break
        else:
            print("Age must be non-negative.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

dog_age = 0

if human_age <= 2:
    dog_age = human_age * 10.5
else:
    dog_age = 2 * 10.5

    remaining_years = human_age - 2

    dog_age += remaining_years * 4
print(f"The dog's age in dog's years is {int(dog_age)} years.")
