numbers=input().split()
ans=[]
cnt=0
for i in range(len(numbers)):
    if int(numbers[i])>0:
        print(numbers[i],end=' ')
    else:
        cnt+=1
print('0 '*cnt)