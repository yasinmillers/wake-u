# Find key with maximum value in dictionary
data = {'a': 5, 'b': 2, 'c': 9, 'd': 1}
max_key = max(data, key=data.get)
print("Key with maximum value:", max_key)