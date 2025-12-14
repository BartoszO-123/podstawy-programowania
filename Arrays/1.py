arr = [2, 3, 7, 5, 4]

print('Array:', arr)

print('Number of elements:', len(arr))

print('First value:', arr[0])

print('Second value:', arr[1])

last_index = len(arr) - 1
print('Last value:', arr[last_index])

second_to_last_index = len(arr) - 2
print('Second-to-last value:', arr[second_to_last_index])

edge_sum = arr[0] + arr[last_index]
print('Sum of the first and last values:', edge_sum)

total_sum = sum(arr)
number_of_elements = len(arr)
average_value = total_sum / number_of_elements
print('Average value:', average_value)

print('All array values separated by a single space:')

for element in arr:
    print(element, end=' ')

print()