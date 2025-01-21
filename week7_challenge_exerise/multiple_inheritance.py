class Birds:
    def fly(self):
        return "Flying like a bird"
    
class Mammal:
    def run(self):
        return "Running like a mammal"
    
class Bat(Birds, Mammal):
    def fly(self):
        return "Flying like a bat"
    
    def run(self):
        return "Running like a bat"

bat = Bat()
print("Bat fly method:", bat.fly())
print("Bat run method:", bat.run())  