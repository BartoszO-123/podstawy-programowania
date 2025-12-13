import keyboard


first_name = keyboard.input_string("Enter name: ")
last_name = keyboard.input_string("Enter surname: ")
age = keyboard.input_integer("Enter age: ")  # --- liczba całkowita ---
salary = keyboard.input_real("Enter salary: ")  # --- liczba rzeczywista ---
is_salary_hidden = keyboard.input_boolean("Hide salary? (y/n): ")

# Drukowanie rekordu pracownika
print("\nDATA RECORD")
print("===========")
print("Name:", first_name)
print("Surname:", last_name)
print("Age:", age)

# Warunkowe drukowanie pensji
if not is_salary_hidden:
    print(f"Salary: {salary:.2f}")
else:
    print("Salary: HIDDEN (Data Protection)")
