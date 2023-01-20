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


