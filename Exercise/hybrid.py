class A:
    def show_A(self):
        print("Method A from class A")
        
class B:
    def show_B(self):
        print("Method B from class B")
        
class C(A, B):
    def show_C(self):
        print("Method C from class C")

class D(C, B):
    def show_D(self):
        print("Method D from class D")
        
        
obj = D()
obj.show_D() 
obj.show_C()  
obj.show_A()  