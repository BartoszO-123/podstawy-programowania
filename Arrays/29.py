array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]
unique_elements = []

for num in array1:
    if num not in array2:
        unique_elements.append(num)

print("\n--- 3.11 ELEMENTS NOT IN SECOND ARRAY ---")
print(f"Array1: {array1}")
print(f"Array2: {array2}")
print(f"Elements in Array1 but not in Array2: {unique_elements}")