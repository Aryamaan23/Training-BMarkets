#Iterators and Generators
class MyIterator:
    def __init__(self,l,h):
        self.l=l
        self.h=h

    def __iter__(self):
        return self

    def __next__(self):
        if self.l<=self.h:
            self.l+=1
            return self.l-1

        else:
            raise StopIteration


it=MyIterator(20,400)
for i in it:
    print(i)



def count(n):
    i=1
    while i<=n:
        yield i
        i+=1

for i in count(5):
    print(i)


#Decorators
def my_decorator(func):
    def inner(n1,n2):
        n=10
        f=func(n1,n2)
        return 10+f

    #Here def inner is closure

    return inner

"""
#Closure means function within function
@my_decorator
def func(n1,n2):
    return n1+n2


n1=int(input('Enter a number'))
n2=int(input('Enter second number'))
print(func(n1,n2))
"""

def doubleval(myfunc):
    def inner(a,b):
        f=myfunc(a,b)
        return f*2
    return inner

@doubleval
@my_decorator
def my_fun(a,b):
    return a**b

print(my_fun(10,2))

