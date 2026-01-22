#Find duplicate values in dictionary
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
duplicate_values = [value for value in my_dict.values() if list(my_dict.values()).count(value) > 1]
print(duplicate_values)