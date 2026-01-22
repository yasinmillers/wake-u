# Filter dictionary with values greater than given number
d = {'a': 10, 'b': 25, 'c': 5, 'd': 30}
n = int(input("Enter a number: "))
filtered_dict = {k: v for k, v in d.items() if v > n}
print(filtered_dict)   