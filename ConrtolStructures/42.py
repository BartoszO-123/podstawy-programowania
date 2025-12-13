time_jacket = 40
time_underwear = 70
time_shoes = 20

time_rinse = 15
time_spin = 9


print("Available programs: (j)acket, (u)nderwear, (s)hoes")
program_input = input("Select washing program: ")


rinse_input = input("Extra rinse? (y/n): ").lower()
extra_rinse = rinse_input == "y"


spin_input = input("Extra spin? (y/n): ").lower()
extra_spin = spin_input == "y"


total_washing_time = 0
washing_product = "Unknown"


if program_input == "j":
    total_washing_time = time_jacket
    washing_product = "jacket"
elif program_input == "u":
    total_washing_time = time_underwear
    washing_product = "underwear"
elif program_input == "s":
    total_washing_time = time_shoes
    washing_product = "shoes"
else:
    print("\nError: Invalid washing program selected. Setting base time to 0.")


if extra_rinse:
    total_washing_time = total_washing_time + time_rinse


if extra_spin:
    total_washing_time = total_washing_time + time_spin


print(f'\nwashing_product = "{washing_product}"')
print(f"rinse = {extra_rinse}")
print(f"spin = {extra_spin}")


print(f"Total washing time: {total_washing_time} minutes")
