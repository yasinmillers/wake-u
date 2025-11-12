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

  
class Dog(Animal):
    def __init__(self, name, color, age):
        super().__init__(name, species="Canine", type=None, location=None, age=age, color=color, weight=None, height=None, gender=None, diet=None)  
        self.name = name
        self.age = age  
        self.color = color
        self.species = "Canine"  # Class attribute
max= Dog("Max", "Brown", 4)
print(max.name, max.age, max.species, max.color)  

class Cat(Animal):
    def __init__(self, name, color, age):
        super().__init__(name, species="Feline", type=None, location=None, age=age, color=color, weight=None, height=None, gender=None, diet=None)  
        self.name = name 
        self.color = color 
        self.age = age      
        self.species = "Felineafrica"  # Class attribute
bella = Cat("Bella", "Black", 3)
print(bella.name, bella.age, bella.species, bella.color)
           
                             