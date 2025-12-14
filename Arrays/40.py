array1 = [2, 4, 6]
array2 = [1, 2, 3, 4, 5, 6, 7]
is_subset = True

for element in array1:
    if element not in array2:
        is_subset = False
        break

print("\n--- 3.22 CHECK FOR SUBSET ---")
print(f"Array1: {array1}")
print(f"Array2: {array2}")
if is_subset:
    print("Result: Array1 is a subset of Array2")
else:
    print("Result: Array1 is NOT a subset of Array2")