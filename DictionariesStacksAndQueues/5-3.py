# Dictionary containing English to Polish translations
translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

# Get user input
word = input('Enter a word in English: ').lower().strip()

# Check if the word exists in the dictionary
if word in translations:
    print(f'Translation: {translations[word]}')
else:
    print('Information: The translation is unavailable.')