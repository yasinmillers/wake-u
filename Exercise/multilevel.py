class Grandparent:
    def family1(self):
        return "Grandparent"
    
class Parent(Grandparent):
    def family2(self):
        return "Parent"

class Child(Parent):
    def family3(self):
        return "Child"
    
obj = Child()
obj.family3()
obj.family2()
obj.family1()
print(obj.family3())  
print(obj.family2()) 
print(obj.family1())  
obj2 = Parent()
print(obj2.family2())
print(obj2.family1())