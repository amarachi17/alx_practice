class Animal:
    def eat(self):
        print("This animal is eating.")
        
    def sleep(self):
        print("This animal is sleeping.")
        
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")
        
animal = Animal()
animal.eat()
animal.sleep()

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()