f=open('test.txt','r')
frequency=[]
line=f.read().split()
for i in line:
    frequency[i]=0
for i in line:
    frequency[i]+=1
for i in line:
    print(f'{i}:{frequency[i]}')
f.close()