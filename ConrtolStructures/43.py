time_24h_input = input("Wprowadź czas (hh:mm): ")
konwersja_udana = True

try:
    godzina_24h_str, minuty_str = time_24h_input.split(":")
    godzina_24h = int(godzina_24h_str)
    minuty = int(minuty_str)

    if not (0 <= godzina_24h <= 23 and 0 <= minuty <= 59):
        konwersja_udana = False
        print("Błąd: Godzina musi być w zakresie 00-23, a minuty 00-59.")

except ValueError:
    konwersja_udana = False
    print("Błąd: Niepoprawny format lub wartości.")
except Exception:
    konwersja_udana = False
    print("Błąd: Wprowadzony format musi być 'hh:mm'.")


if konwersja_udana:
    przyrostek = "pm" if godzina_24h >= 12 else "am"

    godzina_12h = godzina_24h % 12

    if godzina_12h == 0:
        godzina_12h = 12

    print(f"Czas w formacie 12-godzinnym: {godzina_12h}:{minuty_str}{przyrostek}")
