# Create a class
from unicodedata import name


class Person:
   def __init__(self,name,age):
       
        self.name=name
        self.age=age

   def greet(self):
       print("Hello,my name is",self.name)


    
# Create an object
p1=Person("john",5)

# Call the greet method
p1.greet()
