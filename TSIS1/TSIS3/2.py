numbers=input().split()
min_number=1000
for i in range(len(numbers)):
    x=int(numbers[i])
    if x>0 and x < min_number: min_number=x
print(min_number)