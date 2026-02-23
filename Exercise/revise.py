# define parent class
class Parent: 
   def myMethod(self):
      print ('Calling parent method')

# define child class
class Child(Parent): 
   def myMethod(self):
      print ('Calling child method')

# instance of child
c = Child() 
# child calls overridden method
c.myMethod()
class example:
    def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))