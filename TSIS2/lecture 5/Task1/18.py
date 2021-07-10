f=open('test_18.txt','r')
text=f.read()
text.replace(',',' ')
print(len(text.split(' ')))