l=[1,2,3,3,3,3,4,5]
x = []
for a in l:
    if a not in x:
        x.append(a)
print(x)