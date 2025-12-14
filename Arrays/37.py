def bubble_sort(arr):
    n = len(arr)
    temp_arr = arr[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp_arr[j] > temp_arr[j + 1]:
                temp_arr[j], temp_arr[j + 1] = temp_arr[j + 1], temp_arr[j]
    return temp_arr


def get_second_largest(arr):
    sorted_arr = bubble_sort(arr)
    if len(sorted_arr) < 2:
        return None
    return sorted_arr[-2]


def get_range_difference(arr):
    min_val = arr[0]
    max_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return max_val - min_val


def get_median(arr):
    sorted_arr = bubble_sort(arr)
    n = len(sorted_arr)
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        mid1 = sorted_arr[n // 2 - 1]
        mid2 = sorted_arr[n // 2]
        return (mid1 + mid2) / 2


def get_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return [min_val, max_val]


def array_to_string(arr):
    return "-".join(map(str, arr))


numbers = [7, 3, 8, 5, 2]

print("\n--- 3.19 ARRAY MODULE FUNCTIONS ---")
print(f"Numbers: {','.join(map(str, numbers))}")

print("Second largest number:", get_second_largest(numbers))
print("Median:", get_median(numbers))
min_max_array = get_min_max(numbers)
print(f"Smallest and largest number: {min_max_array[0]},{min_max_array[1]}")
print("Numbers as a string:", array_to_string(numbers))
