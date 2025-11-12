class Animal:
    def __init__(self, name, species,type,location,age,color,weight,height,gender,diet):
        self.name = name
        self.species = species
        self.type = type
        self.location = location
        self.age = age
        self.color = color
        self.weight = weight
        self.height = height
        self.gender = gender
        self.diet = diet

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")