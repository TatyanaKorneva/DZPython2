n=input()
s=0
for i in n:
    if i in "1234567890":
        s=s+int(i)
print(s)

# Решение 2
n=input()
s=0
for i in range(len(n)):
    if n[i] in "1234567890":
       s=s+int(n[i])
print(s)
