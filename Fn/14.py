import range_check
import keyboard


RANGE_START = 2
RANGE_END = 15


number = keyboard.input_integer("A number: ")


result = range_check.is_in_range(number, RANGE_START, RANGE_END)


answer = "yes" if result else "no"


print(f"Number {number} in the range <{RANGE_START},{RANGE_END}>: {answer}")
