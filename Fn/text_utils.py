def count_letter(text, letter):
    text_lower = text.lower()
    letter_lower = letter.lower()
    
    return text_lower.count(letter_lower)