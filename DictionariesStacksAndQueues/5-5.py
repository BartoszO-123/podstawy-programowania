paragraph = "cat dog mouse cat rat cat mouse"

# Split the paragraph into individual words 
words = paragraph.split()

# Create an empty dictionary to store word counts
word_counts = {}

# Iterate through each word in the list
for word in words:
    # Check the dictionary to see if the next word appears in it [cite: 1, 2, 3]
    if word in word_counts:
        # If so, increase the number of times the word appears by 1 
        word_counts[word] += 1
    else:
        # If not, add the word to the dictionary with a count of 1
        word_counts[word] = 1

# Print the results
print("Word frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")