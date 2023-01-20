import py_compile
py_compile.compile('main.py')
print('Akshit the snapchatter')

x=3
if not x:
    print('it is 3')
else:
    print('it is 3')

a=10
b=20
a,b=b,a
print(a)
print(b)
temp=a
a=b
b=temp

# single line comment
"""
multi - line comment
"""
"""
If-else if ladder

We can use and or in order to combine the conditions
if cond:


elif cond:

else:

Loops 

for i in range(0,n):
    print(i)

There are no increment or decrement operators in python
In order to increment or decrement the value of the variable we use 
c=c+1 or c=c-1 or c+=1 or c-=1


"""

#This two terms will be printed by space
print ("Hello","xyz")
#In the end parameter the delimeter can be changed
#print ("Hello","xyz",end=" ")

x=3
y=3


#Assignment

# Star pattern matching
def triangle(n):
    k = n - 1
 
    for i in range(0, n):
     
        for j in range(0, k):
            print(end=" ")
     
        k = k - 1
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
        print("\r")
 
n = 3
triangle(n)
 
# Doc string concept 
def my_func():
    '''This is my function and this is the description.'''
    return None

print(my_func.__doc__)


#Q2. Pattern of alphabets
# outer loop
for i in range (65,70):
    k=i
    # inner loop
    for j in range(65,i+1):
        print(chr(k),end="")
        k=k+1
    print()


#doc is membership operator

class X:
    """
    This is X
    """
    pass


#Slicing never gives you error , it will remain empty
sa="I am learning python"
print(sa[5:10])
print(sa[5:10:3])
print(sa[10:5:-1])
print(sa[:3:-1])
s="xyz:345:12161"
s=s.split(":")
print(s)

#For pattern recognition
print(sa.find("a",3,10))
print(sa.find("py"))

#To join the strings
l=["Hello","there","Pune"]
s2=" ".join(l)
print(s2)


print("{:5d}".format(12))
print("{:2d}".format(1234))
print("{:8.3f}".format(12.2346))
print("{:05d}".format(12))
print("{:08.3f}".format(12.2346))
print("{:^10.3f}".format(12.2346))
print("{:<05d}".format(12))
print("{:>08.13f}".format(12.2346))
print("{:=8.3f}".format(-12.2346))

print("Hello {} your balance is {}".format("kapil",4563))
name = 'Aryamaan'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

txt = "     banana     "
x = txt.strip()
print(x)

#Assignment

#Count no of occurences of character in python

s="I am learning python"

freq={}
for ele in s:
    if(ele in freq):
        freq[ele]+=1
    else:
        freq[ele]=1
print('Occurences of each character in a string: \n' + str(freq))


#2nd method
from collections import Counter

a_string = 'the quick brown fox jumps over the lazy dog'
collection = Counter(a_string)

print(collection)


#List functions
"""
L.reverse()
L.pop()
L.index()
L.find()
L.count()
L.remove(10)
L.append()s
"""

#Tuple functions
"""
T=()
T=tuple()
T=(1,) Single element tuple
count()
index()

"""

#Dictionary
"""
d={}
d=dict()
d["Red"]="Apple"
d={"Red":"Apple","Yellow":"Banana"}
d["Red"]
D.get("Red")
for k in D:
    print(k,D[k])

for k in D.keys():
    print(k,D[k])
"""

#Conversion of list to dict
fruits=["Apple","Banana","Pear","Peach"]
print(fruits)
fruit_d=dict.fromkeys(fruits,"In Stock")
print(fruit_d)

#Formation of dic from lists using zip function
L1=["India","China","Sri Lanka"]
L2=["Pune","Beijing","Colombo"]
d=dict(list(zip(L1,L2)))
print(d)

#Nested dictionary
people={1: {'name':'Aryamaan','age':'22','school':'SJC'},
        2: {'name':'Akshit','age':'23','school':'BHS'},
        3: {'name':'Tanuj','age':'22','school':'MLS'}}
print(people[2]['age'])

#Adding data to the dictionary
people[4]={}
people[4]['name']='Karan'
people[4]['age']='23'
people[4]['school']='GHS'

print(people)

# del people[3], people[4]

for p_id,p_info in people.items():
    print("\nPerson ID:",p_id)

    for key in p_info:
        print(key+':'+p_info[key])


#Sorting the dictionary
#print(d.sorted())

#Sets
S=set()
S1={1,2,3,4,5,6,7,8,9,10}
S2={11,12,13,14,15}
print(S1.union(S2))
print(S1.difference(S2))
print(S1.symmetric_difference(S2))
print(S1.intersection(S2))

#Functions
"""
A block of statements with some specific taskss
def func():
    print('Hello')

It is used for code reusability

func()
"""

#This kind of program is a bug, logical error
def func(my_list):
    my_list.append(100)

L=[1,2,3,4]
print(L)
func(L)
print(L)

#Factorial of a number
def fact(n):
    if(n==0 or n==1):
        return n
    return n*fact(n-1)

print(fact(5))


#String reversal
s=input()
rs=s[::-1]
print(rs)


#lambda functions
x=lambda x,y:x+y
print(x(10,20))

L=[1,2,3,4]
L=list(map(lambda x: x**3,L))
print(L)
L=list(filter(lambda x:x%2==0,L))
print(L)

from functools import reduce
L=reduce(lambda x,y:x+y,L)
print(L)

"""
File Handling

File Modes: "w","wt","r","rt","a","
f=open(filename,mode)

f=open("home/xyz/test.txt",w)
f.write("This is my file")
f.write("second line")
f.close()

for line in f:
    print("f)
line=f.readline()
line=f.read()
f.read(10)

with open(filename,mod) as f:


"""

with open('text.txt',"r") as f:
    print(f.seek(0))
    for line in f:
        
        print(line)

with open('text.txt',"a") as f:
    f.write('\n5.Gowtham')
    f.write('\n6.Siddharth')


with open('text.txt',"r") as f:
    for line in f:
        
        print(line)

with open('text.txt',"r") as f:
    print(f.seek(0))
    for line in f:
        
        print(line)


#Changing the contents of a file using temporary file

#importing necessary functions and modules
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
#store the path of the file in a variable
path="demo.txt"
#define the replace function
def replace(file_path, Avengers, Finxters):
    
   #Create temp file
   fd, abs_path = mkstemp()
   with fdopen(fd,'w') as new_file:
       with open(file_path,'r') as old_file:
           for line in old_file:
               new_file.write(line.replace(Avengers,Finxters))
               
   #Copy the file permissions from the old file to the new file
   copymode(file_path, abs_path)
   
   #Remove original file
   remove(file_path)
   
   #Move new file
   move(abs_path, file_path)
   
#calling the replace() method
replace(path,'Akshit','Karan')
replace(path,'Akshit','Bengu Boi')


#OOPs - Object Oriented Programming

#class Emp:
#    def p(self):
#        print('A')

#a=Emp()
#a.p()

#___init__ is used to initialize the objects of a class
# self represents the instance of the class. By using the “self” we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
class Person:
  __a='Aryamaan'#private member
  _b=1212 #protected member
  def __init__(self, name, age,eid):
    self.name = name
    self.age = age
    self.eid=eid
if __name__=='__main__':
    p1 = Person("John", 36,1223232)
    p2=Person("Aryamaan",22,121212121)
    print(p1.name)
    print(p1.age)
    print(p1.eid)
    print(p2._Person__a) #Method for accessing private member
    print(p1._b)#Method for accessing protected member




#Converting list to a dictionary and pushing it to the pandas data frame
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
 
 
# Driver code
lst = ['a', 1, 'b', 2, 'c', 3,'d',4,'e',5]
print(Convert(lst))

#import pandas as pd
#df1=pd.DataFrame(Convert(lst))


#Importing file as a module
import Python.demo as d
d.convert({
  "name": "John",
  "age": 30,
  "city": "New York"
}
)
"""
class Emp():
    x=1000
    #org="Bajaj"
    def __init__(self,eid,ename,esal=30000):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def display(self):
        print('EID\tENAME\tESAL')
        print(self.eid,"\t",self.ename,"\t",self.esal)

@staticmethod
def static_demo(n):
   Emp.x=2000

#@classmethod
#def modify(cls,n):
#    cls.org=n


e1=Emp("E01","Aryamaan",30000)
print(e1.x)
static_demo(2000)
print(e1.x)

"""

"""
class Emp:
    x = 10000
    def __init__(self,eid,ename,esal=30000):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        print("EID\t Ename\t Esal")
        print(self.eid,"\t", self.ename,"\t", self.esal)
    
@classmethod
def modify(cls,n):
    cls.x = n

@staticmethod
def static_demo(n):
    Emp.x = 2000

e1 = Emp("EO1","Askhit", 30000)
print(e1.x)
static_demo(3000)
print(e1.x)

"""

class Emp:
    x = 10000
    def __init__(self,eid,ename,esal=30000):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        print("EID\t Ename\t Esal")
        print(self.eid,"\t", self.ename,"\t", self.esal)
    
    @classmethod
    def modify(cls,n):
        cls.x = n

    @staticmethod
    def static_demo(n):
        Emp.x = 3000

#e1 = Emp("EO1","Askhit", 30000)
#print(e1.x)
e2=Emp('E01','Akshit',2000)
e2.static_demo(3000)
e2.modify(4000)
print(e2.x)


# Args and kwargs Keyword
def my_func(*args,**kwargs):
    print(type(args),type(kwargs))
    print(args,kwargs)

    for a in args:
        print(a,end="")

    for k,v in kwargs.items():
        print(k,v,end=" ")

my_func(1,2,3,4,5,x=4,y=6,z=10,a=11)
print('\n')

##Very important for debugging and routing
"""
pdb> h-help
l-10 lines
n-next
r-run
-step is used for going inside the function


import pdb
pdb.set_trace()
After executing this line number will be denoted as checkpoint
"""

class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]

    def give_raise(self,percent):
        self.pay=int(self.pay+(self.pay*percent/100.0))

    def __repr__(self):
        return "[Person: %s Pay: %s]" % (self.name,self.pay)

    def __str__(self): #human readable format
        return "xyz"

    


bob=Person('Bob Smith',job='IAS',pay=1212212)
sub=Person('Sub Jones',job='dev',pay=100000)
bob.give_raise(20)
sub.give_raise(20)
print(sub.lastName(),"pay= ",sub.pay)
print(bob.lastName(),"pay= ",bob.pay)
print(bob.__repr__())
print(bob.__str__())


import datetime
now=datetime.datetime.now()
print(now.__str__())
print(now.__repr__())


"""
class Book1:
    def _init_(self,pages):
        self.pages = pages
    def _add_(self,other_ob):
        return self.pages + other_ob.pages

class Book2:
    def _init_(self,pages):
        self.pages = pages
    def _gt_(self,ob):
        return self.pages > ob.pages
    
b1 = Book1(100)
b2 = Book2(500)
print('Total Pages = ',b1+b2)

if b1>b2: #It will not work because > is overloaded only for b2 so we have to write b2>b1
    print("B2 has more pages")
else:
    print("B1 has more pages")

if b2>b1: #It will work
    print("B2 has more pages")
else:
    print("B1 has more pages")

"""

#re module
import re
p=re.compile(r'm\w\w')
s='car rat mat fat'

r=re.search(r'm\w\w',s)
print(r.group())

s="This;is the: 'core' python\ 's book"
r=re.split(r'\w+',s)
print(r)


s3="an apple a day keeps the doctor away"
r=re.findall(r'a[\w]*',s3)
for w in r:
    print(w)

import urllib.request 
import re

#Assignment
#Read the text file and get the email ids from it
import urllib.request 
import re 
openfile = open('email.txt', 'r')
with openfile as input:
    print (re.findall(r'\b([a-z0-9-_.]+?@[a-z0-9-_.]+)\b', input.read(), re.I))


#Read the text file and get the dates from it
f=open('date.txt','r')
with f as input:
    content=f.read()
    print(content)
    pattern=r"\d+/+\d+/+\d+"
    dates=re.findall(pattern,content)
    for date in dates:
      print(date)


#Assignment
url = r"https://raw.githubusercontent.com/tokern/piicatcher/master/tests/samples/sample-data.csv"

from urllib.request import urlopen

def read_data(url):
    if url.startswith(('http:','https:','ftp:')):
        return urlopen(url).read()

    else:
        print('Not valid url')

s=read_data(url).decode('utf-8')
#print(s)
print(type(s))

def Convert(string): 
    li = list(string.split("\r\n")) 
    records=[]
    for l in li:
        records.append(l.split(","))
    return records
records = Convert(s)
print(records[1])

print('Python is cool!')

#Inheritance
'''
class Student:
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def get_stud_info(self):
        return self.name,self.age
    def set_stud_info(self,name,age):
        self.name = name
        self.age = age
    
class ScienceStudent(Student):
    def _init_(self, name, age):
        super()._init_(name, age)
    def get_sub(self):
        return "Science"

s = ScienceStudent("Ram", 20)
print(s.get_stud_info())
s.set_stud_info("Ragul", 21)
print(s.get_stud_info())
print(s.get_sub())
'''


