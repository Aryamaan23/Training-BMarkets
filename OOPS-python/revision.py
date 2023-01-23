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