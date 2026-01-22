class MyClass:
    my_variable = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age
m1 = MyClass("Alice", 30)
m2= MyClass("Bob", 25)
print(m1.name, m1.age)
print(m2.name, m2.age)
print(MyClass.my_variable)
MyClass.my_variable=20
print(MyClass.my_variable)

