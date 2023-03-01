n=int(input("Enter a number : "))
sum=0
count=len(str(n))
temp=n
while(n>0):
    r=n%10
    sum+=r**count
    n=n//10
print(sum)
if sum==temp:
    print("Armstrong Number")
else:
    print("Not an armstrong number..")