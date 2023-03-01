#Display all 3 digited Armstrong numbers.
for i in range(100,999+1):
    sum=0
    temp=i
    while(i>0):
        r=i%10
        sum+=r**3
        i=i//10
    if sum==temp:
        print(temp)
