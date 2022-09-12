import random
n=int(input())
s=[]
for i in range(-n, n+1):
    s.append(i)
    random.shuffle(s)
print(s)



