

import months
import keyboard


month_number = keyboard.input_integer("Enter month number: ")


month_name = months.month(month_number)


if month_name != "Invalid month number":
    print(f"The name of month {month_number} is {month_name}")
else:
    print(f"Error: {month_name}")
