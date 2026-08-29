#Parent Class
class familymember:
    def __init__(self,eyes,height_cm):
        self.eyes = eyes
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye color:", self.eyes)
        print("height in cm:", self.height_cm)

#Child Class
class Kid(familymember):
    def __init__(self,name,age,eyes,height_cm):
        self.name = name
        self.age = age
        super().__init__(eyes,height_cm)

    def show_traits(self):
        print("Name", self.name)
        print("Age", self.age)
        super().show_traits()

    def fav_hobby(self,hobby):
        print(f"{self.name} has a hobby which is {hobby}")

child = Kid("maya", "13", "blue", 150)
child.show_traits()
child.fav_hobby("playing video games")