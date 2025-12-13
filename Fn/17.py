import coin_counter

# Testowanie przykładów
print(f"f(23) returns {coin_counter.f(23)}")
print(f"f(8) returns {coin_counter.f(8)}")
print(f"f(2) returns {coin_counter.f(2)}")
print(f"f(0) returns {coin_counter.f(0)}")

# Przykład interaktywny
# Ostrzeżenie: jeśli użytkownik wpisze tekst, program zakończy się błędem ValueError
amount = int(input("\nEnter amount to pay: "))

if amount >= 0:
    min_coins = coin_counter.f(amount)
    print(f"f({amount}) returns {min_coins}")
