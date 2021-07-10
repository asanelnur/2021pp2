text='The quick Brow Fox'
Uppercasecharacters=0
Lowercasecharacters=0
for i in text:
    if i.isupper():
        Uppercasecharacters+=1
    if i.islower():
        Lowercasecharacters+=1
print ("Original String : ", text)
print ("No. of Upper case characters : ", Uppercasecharacters)
print ("No. of Lower case Characters : ", Lowercasecharacters)