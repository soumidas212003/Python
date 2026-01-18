r=int(input("Enter the range: "))
count=1
sum=0
for i in range(1,r+1):
    print(count,end="+")
    sum+=count
    count+=i
print("\b=",sum) 