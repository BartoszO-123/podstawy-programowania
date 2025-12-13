def f(amount_to_pay):
    """
    Zwraca minimalną liczbę monet (1, 2 i 5 zł) potrzebnych do zapłacenia kwoty.
    """

    # Dostępne monety w kolejności malejącej
    coins = [5, 2, 1]
    count = 0
    remaining_amount = amount_to_pay

    for coin in coins:
        # 1. Oblicz, ile razy największa moneta mieści się w pozostałej kwocie
        num_coins = remaining_amount // coin

        # 2. Dodaj tę liczbę monet do sumy całkowitej
        count += num_coins

        # 3. Zaktualizuj pozostałą kwotę (reszta z dzielenia)
        remaining_amount %= coin

    return count
