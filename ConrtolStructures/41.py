ean_length = 13
poland_prefix = "590"


ean_number = input("Enter EAN-13 article number: ")


is_correct_length = False


if len(ean_number) == ean_length:
    is_correct_length = True
    print("Article number is correct")

    if ean_number[0:3] == poland_prefix:
        print("Article manufactured in Poland")

else:
    print(f"Error: Article number must be exactly {ean_length} characters long.")
