class A:
    def display(self):
        print("This is class A")
        
        
class B(A):
    def display(self):
        print("This is class B")  

class C(A, B):
    def display(self):
        print("This is class C")

obj_a = A()
obj_a.display()  
obj_b = B()
obj_b.display()  
obj_c = C()
obj_c.display()

            