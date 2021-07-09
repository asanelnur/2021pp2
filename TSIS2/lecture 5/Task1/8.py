f=open('test.txt','r')
b=list()
b=f.read().split()
max_size=0
ans=''
for i in b:
    if len(i)>max_size:
        max_size=len(i)
        ans=i
print(ans)
f.close()