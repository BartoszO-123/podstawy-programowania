arr = [1, 2, 3, 4, 5]

print("Array:", arr)


arr[0] = arr[0] - 1
print("Array:", arr)


arr[len(arr) - 1] = arr[len(arr) - 1] + 4
print("Array:", arr)

middle_index = (len(arr) - 1) // 2
arr[middle_index] = arr[middle_index] * 2
print("Array:", arr)
