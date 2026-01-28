class Parent:
    def show_parent(self):
        print("This is the Parent class")
    
class Child(Parent):
    def show_child(self):
        print("This is the Child class")
    
# Example usage
obj = Child()
obj.show_child()   # Method from Child class