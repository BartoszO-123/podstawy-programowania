import re

text = input("Enter text: ")


number_of_words = len(re.findall(r"[aeiouyAEIOUY]", text))

print(f"Number of vowels: {number_of_words}")
