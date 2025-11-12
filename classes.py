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

  
cow = Animal("Bessie", "Mammal","Herbivore","Farm",5,"Brown",1500,60, " Female","Grass")
goat = Animal("Billy", "Mammal","Herbivore","Farm",3,"White",200,30, "Male","Grass")
cat = Animal("Whiskers", "Mammal","Carnivore","House",2,"Black",15,10, "Female","Fish")
fox = Animal("Foxy", "Mammal","Omnivore","Forest",4,"Red",30,20, "Male","Small animals and fruits")
print(cow.name, cow.species, cow.type, cow.location, cow.age, cow.color, cow.weight, cow.height, cow.gender, cow.diet)       