f=open('test.txt','r')
line=f.readlines()
array=[]
for i in line:
    array.append(i)
print(array)
f.close()