import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('test.txt'))
f=open('test.txt','r')
lines=f.read().split()
answer=random.choice(lines)
print(answer)
f.close()