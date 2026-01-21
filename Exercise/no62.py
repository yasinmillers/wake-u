#Remove a key from dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = input("Enter a key to remove: ")
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print("Key removed successfully.")
else:
    print("Key not found.")
print(my_dict)  