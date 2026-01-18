n=int(input("Enter the digit : "))
count=0
while n>0:
    r=n%10
    count+=r
    n=n//10
print(count)