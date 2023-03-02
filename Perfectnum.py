#6(1 2 3 =6)
n=int(input("Enter a number: "))
count=0
for i in range(1,n):
   if n%i==0:
      print(i,end="  ")
      count+=i
      i+=1 
print("\ncount=",count)
if count==n:
      print("perfect number")
else:
    print("Not perfect")