n=int(input())
i=2
if n==1:
    res=False
elif n==2:
    res=True
else:
    res=True
    while i<n:
        if n%i==0:
            res=False
            break
        i+=1
if res:
    print(n,' is prime')
else:
    print(n,' is not prime')