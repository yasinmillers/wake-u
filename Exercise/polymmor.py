class Vehicle:
    def rent(self):
        pass
    
    
class Car(Vehicle):
    def rent(self):
        print("car is rented at 200 per day")
class Bike(Vehicle):
    def rent(self):
        print("bike is rented at 50 per day")
class Truck(Vehicle):
    def rent(self):
        print("truck is rented at 500 per day")     
        
        
vehicle=[Car(), Bike(), Truck()]
for v in vehicle:
    v.rent()         