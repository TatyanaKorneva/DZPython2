x=input()
y=input()
c = 0
i = -1
f=True
while f==True:
    i = x.find(y, i+1)
    if i == -1:
        f=False
    else:
        c += 1
print(c)

# Решение 2
x=input()
y=input()
print(x.count(y))




