from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can run and walk.")

class Snake(Animal):
    def move(self):
        print("I can crawl.")

class Dog(Animal):
    def move(self):
        print("I can bark.")

h = Human()
h.move()

s = Snake()
s.move()

d = Dog()
d.move()