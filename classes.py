class Animal:
    def __init__(self, name, species,type,location,age,color,weight,height,gender,diet):
        self.name = name
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")