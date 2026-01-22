class MyClass:
    my_variable = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    def show_balance(self):
        print(f"Balance: {self.__balance}")
        
acc=





              
m1 = MyClass("Alice", 30)
m2= MyClass("Bob", 25)
print(m1.name, m1.age)
print(m2.name, m2.age)
print(MyClass.my_variable)
MyClass.my_variable=20
my_variable=30
print(m1.my_variable)
m1.name="Charlie"
print(m1.name)
print(m1.speak())
print(m2.speak())

