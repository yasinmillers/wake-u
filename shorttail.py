from collections import Counter

data = ["a", "b", "a", "c", "a", "b", "d", "e", "f", "g"]

# count frequency
counts = Counter(data)

# sort by frequency
sorted_counts = counts.most_common()

print("All counts:", sorted_counts)

# short tail (top 2 frequent)
print("Short Tail:", sorted_counts[:2])

# long tail (remaining rare items)
print("Long Tail:", sorted_counts[2:])