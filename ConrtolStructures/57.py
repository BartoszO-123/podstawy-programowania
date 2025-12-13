import random

num_count = 20
min_value = 5
max_value = 10

i = 0
while i < num_count:
    random_number = random.randint(min_value, max_value)

    print(random_number, end=" ")

    i += 1

print()
