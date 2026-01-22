class Person:
    def __init__(self, name):
        self.set_name(name)
        
        
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    
    
    
jane = Person("Jane",)
print(jane.get_name())  # Output: Jane

jane.set_name("Janet jackson")
jane.get_name() # Output: Janet jackson
print(jane.get_name())        
        