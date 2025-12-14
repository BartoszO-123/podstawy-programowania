arr = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = []

counts = {}
for item in arr:
    counts[item] = counts.get(item, 0) + 1

for item, count in counts.items():
    if count == 1:
        unique_elements.append(item)

print("\n--- 3.13 UNIQUE ELEMENTS ---")
print(f"Array: {' '.join(map(str, arr))}")
print(f"Unique elements: {' '.join(map(str, unique_elements))}")
