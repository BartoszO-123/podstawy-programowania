def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


array_a = [9, 1, 6, 3, 8]
array_b = [10.5, 3.1, 7.8, 2.2]
array_c = [0, -5, 15, 2]

print("\n--- 3.12 BUBBLE SORT THREE ARRAYS ---")

print(f"Array A before sort: {array_a}")
bubble_sort(array_a)
print(f"Array A after sort: {array_a}")

print(f"Array B before sort: {array_b}")
bubble_sort(array_b)
print(f"Array B after sort: {array_b}")

print(f"Array C before sort: {array_c}")
bubble_sort(array_c)
print(f"Array C after sort: {array_c}")
