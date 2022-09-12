n=int(input())
a=int(input())
b=int(input())
s=[]
for i in range(-n, n+1):
    s.append(i)
print(s, s[a]*s[b], sep='\n')


