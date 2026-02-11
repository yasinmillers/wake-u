# Create a class
class Person:
   def __init__(self,name,age):
        self.name=name
        self.age=age

   def greet(self):
        print("Hello,my name is",name)



# Create an object
p1=Person("john",5)

# Call the greet method
p1.greet()
