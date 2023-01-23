l=[]
for i in range(1,51):
    l.append(i)
print(l)

li=[]
for i in range(1,100):
    if(i%3==0):
        li.append(i)

print(li)



text = open("file.txt", "r")
  

d = dict()
  
for line in text:
    line = line.strip()
    line = line.lower()
  
    words = line.split(" ")
                         
  
    for word in words:
        if word in d:

            d[word] = d[word] + 1
        else:
            
            d[word] = 1
  

#print(d)
#print([k for k, v in d.items() if v == 5])
#for key in list(d.keys()):
#    print(d[key], ":", key)


import re

def main():
    # Reading the file
    with open("file.txt", "r") as f:
        file_in = f.read()
        f.close()
    # Creating the initial dictionary with counts
    d1: dict = {}
    file_in = re.sub('\s+', ' ', file_in)
    words: list = list(map(lambda x: x.lower(), file_in.strip().split(' ')))
    print(words)
    # Iterating over the list of words
    for word in words:
        if word in d1.keys():
            d1[word] += 1
        else:
            d1[word] = 1
    # Creating a count-based dictionary of words
    d2: dict = {}
    for k, v in d1.items():
        if v in d2:
            d2[v].append(k)
        else:
            d2[v] = []
            d2[v].append(k)
    # Displaying the output
    for k, v in d2.items():
        print(k, v)

if __name__ == "__main__":
    main()

f=open('file.txt','r')
data=f.read().lower()
data=data.split()
bow=dict()
for word in data:
    count=data.count(word)
    li=bow.setdefault(count,set())
    li.add(word)

print(li)


#Shallow copy concept
def fun(li):
    li2=li.copy()
    li2.append(1000)
    print(li2)
    return li2


li1=[1,2,3]
li3=fun(li1)
print(li1)
print(li3)


import copy
def fun(li):
    li2=copy.deepcopy(li)
    li2[-1].append('D')
    print(li2)
    return li2


li1=[1,2,3,['A','B']]
li3=fun(li1)
print(li1)
print(li3)

li1=[1,2,3,4]
li2=li1
li3=li2[:]

print(li1==li2)
print(li1 is li2)
print(li3==li1)
print(li3 is li2)
print(li3 is li1)
print(li3 is li2)


l = ['Python','C', 'Java', 'VC++']
a=sorted(l, key=len)
print(a)




import glob
import os

name_of_dir = '/Users/aryamaanpandey'

# Storing list of all files (file paths)
# in the given directory in list_of_files
list_of_files = filter( os.path.isfile,
						glob.glob(name_of_dir + '*') )

# Sort list of files in directory by size
list_of_files = sorted( list_of_files,
						key = lambda x: os.stat(x).st_size)

# Iterate over sorted list of file names
# and print them along with size one by one
for path_of_file in list_of_files:
	size_of_file = os.stat(path_of_file).st_size
	print(size_of_file, ' -->', path_of_file)


lis=[(1,2,3),(4,2,1),(3,4,5),(2,3,4)]
print(sorted(lis,key=lambda x: x[0]))



import os
path='/Users/aryamaanpandey/Desktop/Python-Practice/'
lis=os.listdir(path)
print(sorted(lis,key=lambda x:os.path.getsize(path+x)))

"""

import os
path = r"/Users/aryamaanpandey/Desktop/Python-Practice"
file_list = os.listdir(path)
temp =""
file_dict = dict()
for fl in file_list:
 temp = path + "/" + fl
 file_size = os.path.getsize(temp)
 file_dict[fl] = file_size
 temp = ""
sorted_file_dict = sorted(file_dict.items(), key=lambda kv: kv[1])
print(sorted_file_dict)

"""

txt='Python is easy to learn. It reduces development time'
n = int(input())
res=[]
lis = txt.split()
print(lis)
for pos in range(len(lis)-n+1):
 res.append(lis[pos:pos+n])
print(res)

from itertools import combinations
l=txt.split()
prem=combinations(l,2)
for i in list(prem):
    print(i)