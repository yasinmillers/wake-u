class A:
    def display(self):
        print("This is class A")
        
        
class B(A):
    def display(self):
        print("This is class B")  



obj_a = A()
obj_a.display()  
obj_b = B()
obj_b.display()  

              