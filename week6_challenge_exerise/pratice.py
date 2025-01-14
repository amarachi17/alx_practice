# # How to create a class and use it

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         return "Woof!"
    
# # Creating an instance of the Dog class
# dog1 = Dog("Buddy", "Golden Retriever")
# dog2 = Dog("Max", "German Shepherd")

# # Accessing the object properties
# print(f"{dog1.name} is a {dog1.breed}. He says: {dog1.bark()}")
# print(f"{dog2.name} is a {dog2.breed}. He says: {dog2.bark()}")


class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass
    
# Inheritance
class Lion(Animal):
   def speak(self):
       return f"{self.name} the Lion roars"
class Elephant(Animal):
    def speak(self):
        return f"{self.name} the Elephant trumpets"
    
# Polymorphism

zoo =[
    Lion("Simba"),
    Elephant("Dumbo")
]

for animal in zoo:
    print(animal.speak())