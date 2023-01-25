class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def get_addition(self):
        return self.a+self.b

    def get_difference(self):
        return self.a-self.b

    def get_product(self):
        return self.a*self.b

    def get_division(self):
        return self.a/self.b