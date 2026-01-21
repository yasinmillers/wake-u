#Sort dictionary by values
dict1 = {'a': 1, 'b': 2, 'c': 3}
sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1]))
print(sorted_dict)      