categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)
max_index = expenses.index(max_expense)
most_expensive_category = categories[max_index]


print(f"Category: {most_expensive_category} (Expenses: {max_expense})")
