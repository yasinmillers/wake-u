this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict)
x = this_dict.get("model")
print(x)
this_dict["year"] = 2020
print(this_dict)
this_dict["color"] = "red"
print(this_dict)
this_dict.pop("model")
print(this_dict)
for key in this_dict:
  print(key)
for key in this_dict.keys():
  print(key)
for value in this_dict.values():
  print(value)
for key, value in this_dict.items():
  print(key, value)
if "brand" in this_dict:
  print("Yes, 'brand' is one of the keys in the this_dict dictionary")
print(len(this_dict))