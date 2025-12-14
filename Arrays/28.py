def compare(array1, array2):
    if len(array1) != len(array2):
        return False

    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False

    return True


test_cases = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2]),
]

print("\n--- 3.10 ARRAY COMPARISON ---")
for arr1, arr2 in test_cases:
    result = compare(arr1, arr2)
    comparison_text = "arrays are the same" if result else "arrays are NOT the same"

    print(f"Array1: {' '.join(map(str, arr1))}")
    print(f"Array2: {' '.join(map(str, arr2))}")
    print(f"Comparison: {comparison_text}\n")
