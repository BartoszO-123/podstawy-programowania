def get_words(text):
    import string

    translator = str.maketrans("", "", string.punctuation)
    clean_text = text.translate(translator)
    return clean_text.split()


def count_words(text):
    return len(get_words(text))


def sort_words_by_length(text):
    words = get_words(text)
    return sorted(words, key=len, reverse=True)


def sort_words_alphabetically(text):
    words = get_words(text)
    return sorted(words)


text = "An apple a day keeps the doctor away"

print("\n--- 3.24 TEXT ANALYSIS MODULE ---")
print(f"Text: {text}")

num_words = count_words(text)
print(f"Number of words: {num_words}")

words_by_length = sort_words_by_length(text)
print(f"Words from the longest: {', '.join(words_by_length)}")

words_alphabetically = sort_words_alphabetically(text)
print(f"Words ordered alphabetically: {', '.join(words_alphabetically)}")
