n = int(input()) - 1
f=open('test.txt','r')
line=f.readlines()
line.reverse()
print(*line[n::-1])
f.close()