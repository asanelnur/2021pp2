f = open("test.txt", "r")
text = f.readlines()
f.close()
f=open('13res.txt','w')
for i in text:
        f.write(i)
f.close()
f = open("13res.txt")
print(f.read())