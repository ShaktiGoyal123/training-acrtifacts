from functools import reduce

words = ["apple", "banana", "orange", "apple", "grape", "banana"]

# Count the occurrences of each word
word_counts = reduce(lambda counts, word: {**counts, word: counts.get(word, 0) + 1}, words, {})

print(word_counts)
# Output: {'apple': 2, 'banana': 2, 'orange': 1, 'grape': 1}


numbers = [1, 2, 3, 4, 5]
product = reduce((lambda x, y: x * y), numbers)
