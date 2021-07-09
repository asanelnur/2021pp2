color = ['Red', 'Green', 'White', 'Black']
with open('res.txt', "w") as myfile:
        for k in color:
                myfile.write("%s\n" % k)

content = open('res.txt')
print(content.read())