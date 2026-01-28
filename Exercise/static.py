class Example:
    def instance_method(self):
        return "This is an instance method."
    
    @classmethod
    def class_method(cls):
        return "This is a class method."
    
    @staticmethod
    
    def static_method():
        return "This is a static method."
    
# Example usage
example = Example()
print(example.instance_method()) 
print(Example.class_method())    
print(Example.static_method())    