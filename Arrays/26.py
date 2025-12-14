names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = ""
max_length = 0

for name in names:
    if len(name) > max_length:
        max_length = len(name)
        longest_name = name

print("\n--- 3.8 LONGEST NAME ---")
print(f"Names: {' '.join(names)}")
print(f"Longest name: {longest_name}")