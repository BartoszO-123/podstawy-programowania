import text_utils

TEXT_TO_ANALYZE = "You never get a second chance to make a first impression"
TARGET_LETTER = "e"

count = text_utils.count_letter(TEXT_TO_ANALYZE, TARGET_LETTER)

print(TEXT_TO_ANALYZE)
print(f"The number of letter '{TARGET_LETTER}': {count}")
