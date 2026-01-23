basic_data = {
   "name": "Barbara",
   "age": 21
}

advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# Method 1: Using the union operator (|) - available in Python 3.9+
person = basic_data | advanced_data

# Method 2: Using the update() method (alternative)
# person = basic_data.copy()
# person.update(advanced_data)

# Print the contents of the 'person' dictionary
print(person)