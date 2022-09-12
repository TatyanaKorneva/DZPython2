n=int(input())
l=[]
for i in range(1, n+1):
    if i>1:
        l.append(i*l[i-2])
    else:
        l.append(i)
print(l)
