person1_name = input("Enter first person name: ")
try:
    person1_age = int(input(f"Enter {person1_name}'s age: "))
except ValueError:
    print("Invalid input for age. Assuming not adult.")
    person1_age = 0


person2_name = input("Enter second person name: ")
try:
    person2_age = int(input(f"Enter {person2_name}'s age: "))
except ValueError:
    print("Invalid input for age. Assuming not adult.")
    person2_age = 0


if person1_age >= 18 and person2_age >= 18:
    print(f"\nBoth {person1_name} and {person2_name} are adults.")
else:
    print(f"\nEither {person1_name} or {person2_name} is not an adult.")
