#Create a "Phonebook." Ask the user for a name. Use the .get() method to return
#"Not Found" if the name doesn't exist in your dictionary.
phonebook = {
    "Ssenyonga": "0701122334",
    "Nakato": "0778899001",
    "Kato": "0756677889",
    "Namubiru": "0714455667",
    "Mugisha": "0782233445"
}

# Ask user for a name
name = input("Yingiza erinnya ly’omuntu: ")

# Use .get() with default value
number = phonebook.get(name, "Tewali mu Phonebook")

print(number)