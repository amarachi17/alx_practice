class Dog:
    def make_sound(self):
        return "Woof!"
    
class Cat:
    def make_sound(self):
        return "Meow!"
    
class Bird:
    def make_sound(self):
        return "Chirp!"
    
def let_them_speak(animals):
    for animal in animals:
        print(animal.make_sound())
        
dog = Dog()
cat = Cat()
bird = Bird()

let_them_speak([dog, cat, bird])