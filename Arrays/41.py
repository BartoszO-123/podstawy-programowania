import random


def rand_elem(array):
    return random.choice(array)


arr = [10, 20, 30, 40, 50, 60]

print("\n--- 3.23 RANDOM ARRAY ELEMENT ---")
print(f"Array: {arr}")
print(f"Random element 1: {rand_elem(arr)}")
print(f"Random element 2: {rand_elem(arr)}")
print(f"Random element 3: {rand_elem(arr)}")
