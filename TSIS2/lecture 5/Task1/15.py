import random
f=open('test.txt','r')
lines=f.read().split()
answer=random.choice(lines)
print(answer)
f.close()