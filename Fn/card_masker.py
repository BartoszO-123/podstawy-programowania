def hide(card_number):
    first_two = card_number[:2]
    last_four = card_number[-4:]
    mask_length = len(card_number) - 6
    mask = '*' * mask_length
    return first_two + mask + last_four