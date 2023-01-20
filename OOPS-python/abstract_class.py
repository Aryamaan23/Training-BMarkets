from abc import ABC, abstractclassmethod
class MyClass(ABC):
    @abstractclassmethod
    def calc(self,x):
        pass

class SubClass(MyClass):
    def calc(self,x):
        print("Square= ",x**2)

class MyClass(ABC):
    def connect(self):
        pass

    def disconnect(self):
        pass

ob=SubClass()
ob.calc(15)
