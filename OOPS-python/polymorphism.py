#Class - Based Polymorphism
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f'I am cat,my name is {self.name} and my age is {self.age}')

    def speak(self):
        print('meow')


class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f'I am dog ')

    def speak(self):
        print('Bark')


cat1=Cat('Kitty',3)
dog1=Dog('Fluffy',4)

for animal in (cat1,dog1):
    animal.info()
    animal.speak()



        