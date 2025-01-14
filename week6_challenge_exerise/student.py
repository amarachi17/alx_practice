class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Creating instances of Student class
student1 = Student("John Joe", 32)
student2 = Student("Esther", 42)
student1.display_info()
student2.display_info()


