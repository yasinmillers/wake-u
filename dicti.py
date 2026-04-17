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
my_dict.update({"age": 31})
print(my_dict)
my_dict['road'] = "5th Avenue"
print(my_dict)

keys = []
values = []

for i in range(3):
    k = input("Enter key: ")
    v = input("Enter value: ")
    keys.append(k)
    values.append(v)

my_dict = dict(zip(keys, values))

print("Dictionary:", my_dict)


keys = ["name", "age", "course"]
values = ["Yasin", 20, "Cybersecurity"]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("Dictionary:", my_dict)