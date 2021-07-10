f=open('test.txt','r')
text=f.readlines()
print(s.rstrip('\n') for s in text)
f.close()