class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, color, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        self.color = color  # Instance attribute

dog1 = Dog("Buddy",  'blue',3)  # Create an instance of Dog
dog2 = Dog("Charlie",'white', 5)# Create another instance of Dog
dog3 = Dog("Max",'yellow', 2)    # Create a third instance of Dog


print(dog1.name, dog1.age, dog1.species,dog1.color)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species,dog2.color)  # Access instance and class attributes
print(Dog.species)  