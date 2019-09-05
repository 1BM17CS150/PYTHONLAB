s=input("enter a string")
l=[]
for i in s:
    if i not in l:
        l.append(i)
d={}
c=0
for i in l:
    c=0
    for j in s:
        if i==j:
            c=c+1
    d[i]=c

print(d)
