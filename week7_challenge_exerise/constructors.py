class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person object created: {self.name}, age: {self.age}")
        
    def __del__(self):
        print(f"Person object deleted: {self.name}, age: {self.age}")
        
person1 = Person("Alice", 34)
del person1