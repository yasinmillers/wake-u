#Count words in a sentence using dictionary
sentence = "the quick brown fox jumps over the lazy dog"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)