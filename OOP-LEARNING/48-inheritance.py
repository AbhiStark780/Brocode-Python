# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent


class Animal:
    def __init__(self, name):
        self.name = name
        self.isalive = True
        
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")                           

class Mouse(Animal):
    def speak(self):
        print("chuu")

dog = Dog("scooby")
cat = Cat("garry")
mouse = Mouse("micky")

print(dog.name)
print(dog.isalive)
dog.eat()
dog.sleep()
dog.speak()