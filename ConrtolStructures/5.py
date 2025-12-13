###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.30  # 15%
is_bonus = input("Does the employee receive a bonus? (Y/N):") == "Y" or "y"


if is_bonus:
    total_salary = basic_salary * bonus + basic_salary
else:
    print(basic_salary)


print(f"Basic salary: {basic_salary}")
print(f"Bonus included? {bonus}")
print(f"Total salary: {total_salary}")
