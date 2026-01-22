#Find duplicate values in dictionary
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
duplicate= []
for v in my_dict.values():
    if list(my_dict.values()).count(v) > 1 and v not in duplicate:
        duplicate.append(v)
print(duplicate)