class Example:
    def instance_method(self,name,age):
        return f"This is an instance method for {name}, age {age}."
    
    @classmethod
    def class_method(cls):
        return "This is a class method."
    
    @staticmethod
    
    def static_method():
        return "This is a static method."
    
# Example usage
s=Example("Alice", 30)
example = Example()
print(example.instance_method()) 
print(Example.class_method())    
print(Example.static_method())
print(s.name, s.age )    