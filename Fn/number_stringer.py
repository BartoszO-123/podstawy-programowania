def f(n):
    # Generowanie ciągów znaków dla każdej liczby od 1 do n, a następnie ich łączenie
    return "".join(str(i) for i in range(1, n + 1))