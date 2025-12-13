import math

try:
    N_input = input("Enter the number of leading primes (N) you want to find: ")
    N = int(N_input)

    if N <= 0:
        print("Error: N must be a positive integer.")
        N = 0

except ValueError:
    print("Error: Invalid input. Please enter a whole number for N.")
    N = 0

if N > 0:
    primes = []

    candidate_number = 2

    while len(primes) < N:
        is_prime = True

        limit = int(math.sqrt(candidate_number))

        divisor = 2
        while divisor <= limit:
            if candidate_number % divisor == 0:
                is_prime = False
                break

            divisor += 1

        if is_prime:
            primes.append(candidate_number)

        candidate_number += 1

    print("\nPrime numbers:")
    print(" ".join(map(str, primes)))
