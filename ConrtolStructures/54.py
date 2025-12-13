num_terms = 20

first_term = 0
second_term = 1

output = f"{first_term} {second_term}"

for count in range(2, num_terms):
    next_term = first_term + second_term

    output += f" {next_term}"

    first_term = second_term

    second_term = next_term

print(output)
