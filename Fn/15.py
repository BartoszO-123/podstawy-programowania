import card_masker

CARD = "5290312400019022"

masked_card = card_masker.hide(CARD)

print(f'"{CARD}" returns "{masked_card}"')
