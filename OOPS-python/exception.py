'''
try:
    f=open('file.txt',"w")
    a,b=[int(x) for x in input('Enter 2 numbers: ').split(" ")]
    c=a/b
    f.write('writing %d into file', c)

except ZeroDivisionError:
    print("")
'''

'''
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  '''

'''
def avg(l):
    t=0
    for i in l:
        t+=i
    avg=t/len(l)
    return t,avg

try:
    t,a=avg([1,2,3,4,"p"])
    print(f"total = {t} ,avg={a}")

except TypeError as te:
    print(te)
except ZeroDivisionError as ze:
    print(ze)

'''

#Raise Excepition
'''
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

'''
class MyException(Exception):
    def __init__(self,arg):
        self.arg=arg


def check(d):
    for k,v in d.items():
        print(k,v)
        if(v<2000.0):
            raise MyException('Balance is 0')

b={'Raj':4000,'Ramesh':3000,'Mahesh':1000,'Ram':400}
try:
    check(b)
except MyException as me:
    print(me)

