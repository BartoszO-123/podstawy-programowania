def occurs(number, array):
    return number in array


arr = [15, 38, 7, 23, 14]

number_to_check = 23

result = occurs(number_to_check, arr)
result_text = (
    f"number {number_to_check} appears in the array"
    if result
    else f"number {number_to_check} does NOT appear in the array"
)

print("\n--- 3.14 NUMBER OCCURRENCE ---")
print(f"Number: {number_to_check}")
print(f"Array: {' '.join(map(str, arr))}")
print(f"Result: {result_text}")
