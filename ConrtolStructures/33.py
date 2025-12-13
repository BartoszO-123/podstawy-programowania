while True:
    try:
        age = int(input("Please enter your age: "))

        if age >= 0:
            break
        else:
            print("Age cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")


age_group = ""


if age < 13:
    age_group = "Child"

elif age <= 19:
    age_group = "Teen"

elif age <= 64:
    age_group = "Adult"

else:
    age_group = "Senior"

print(f"Your age is: {age}")
print(f"You belong to the age group: {age_group}")
