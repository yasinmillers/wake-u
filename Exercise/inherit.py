class Person:
    
    def __init__(self, name):
        self.name=name
        
    def show(self):
        return self.name  
    
  
class Student(Person):
    
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        
    def get_student_info(self):
        return f"Name: {self.name}, Student ID: {self.student_id}"
            
# Example usage
student = Student("Alice", "S12345")
student.show()
print(student.get_student_info())  


    