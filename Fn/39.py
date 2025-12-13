def sum_natural(n):
    if n == 1:
        return 1

    return n + sum_natural(n - 1)


n = 10
result = sum_natural(n)

print(f"Obliczanie sumy liczb naturalnych z zakresu <1, {n}>:")
print(f"Suma = 1 + 2 + 3 + ... + {n}")
print(f"Wynik: {result}")
