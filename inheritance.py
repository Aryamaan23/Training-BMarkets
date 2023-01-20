class Animal:
    def __init__(self,animal):
        self.animal = animal
        print(self.animal, "is an Animal")

class Mammal(Animal):
    def __init__(self,mname):
        print(mname,"is a warm blooded")
        super().__init__(mname)

class NonWingedMammal(Mammal):
    def __init__(self,nwmammal):
        print(nwmammal, "cant fly")
        super().__init__(nwmammal)

class NonMarineMammal(Mammal):
    def __init__(self,nmmammal):
        print(nmmammal, "can't swim")
        super().__init__(nmmammal)

class Dog(NonMarineMammal,NonWingedMammal):
    def __init__(self):
        print("Dog has four legs")
        super().__init__('Dog')


d = Dog()
