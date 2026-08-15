class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 12)
woody = Parrot("Woody", 10)

print(f"{blu.name} is a {blu.species}, and is {blu.age} years old.")
print(f"{woody.name} is a {woody.species}, and is {woody.age} years old.")