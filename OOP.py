class Animal:
    def __init__(self, name):
        self.name = name
    
    def dog(self):
        print(f"{self.name} is a dog")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def dog(self):
        print(f"{self.name} is a {self.breed} dog")
dog = Dog("Tommy", "Labrador")
dog.dog()
