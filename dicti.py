my_dict= {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "year" : 2024,
    "place": "USA",
    "dob": "1994-05-15"
    
}
print(len(my_dict))
print(type(my_dict))
print(my_dict)
print(my_dict["name"])
print(my_dict.items( ))
if 'city' in my_dict:
    print("City is present in the dictionary.")
else:
    print("City is not present in the dictionary.") 