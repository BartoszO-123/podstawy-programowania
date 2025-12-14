monthly_expenses = [[200, 50, 100], [180, 60, 110], [220, 55, 105], [210, 65, 95]]

categories = ["Food", "Transport", "Utilities"]
num_categories = len(categories)
num_weeks = len(monthly_expenses)

category_totals = [0] * num_categories
week_totals = [0] * num_weeks

for i in range(num_weeks):
    week_sum = 0
    for j in range(num_categories):
        expense = monthly_expenses[i][j]
        category_totals[j] += expense
        week_sum += expense
    week_totals[i] = week_sum

total_monthly_expenses = sum(week_totals)

print("\nMONTHLY EXPENSES")
print("-------------------------------------")

print("EXPENSES BY CATEGORY:")
print(f"Food: {category_totals[0]}")
print(f"Transport: {category_totals[1]}")
print(f"Utilities: {category_totals[2]}")

print("\nEXPENSES BY WEEK:")
print(f"Week 1: {week_totals[0]}")
print(f"Week 2: {week_totals[1]}")
print(f"Week 3: {week_totals[2]}")
print(f"Week 4: {week_totals[3]}")

print("----------------")
print("TOTAL:", total_monthly_expenses)
