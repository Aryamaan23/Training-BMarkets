#Method overriding there is no overloading
from math import pi;
class Shape:
    def __init__(self,name):
        self.name=name

    def area(self):
        pass

    def fact(self):
        return "2D Shape"

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self,length):
        super().__init__('Square')
        self.length=length

    def area(self):
        return self.length**2

    def fact(self):
        return "each angle is 90 degree"


class Circle(Shape):
    def __init__(self,r):
        super().__init__("Circle")
        self.r=r

    def area(self):
        return pi*self.r**2

a=Square(4)
b=Circle(5.6)
print(b)
print(b.fact())
print(a)
print(a.fact())
print(b.area())
print(a.area())



