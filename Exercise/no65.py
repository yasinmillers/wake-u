#Invert keys and values in a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value: key for key, value in my_dict.items()}
print(inverted_dict)