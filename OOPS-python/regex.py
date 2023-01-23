import re
dxn={}
with open("file.txt" , "r") as f:
    for line in f.readlines():
        for x in line.split():
            if x.isalpha():
                if re.match("\w+", x, re.IGNORECASE):
                    if x in dxn:
                        dxn[x] +=1
                    else:
                        dxn[x]=1
 
res={}
for key, val in dxn.items():
 if val in res:
    res[val].append(key)
 else:
    res[val] = []
    res[val].append(key)
print(res)