#1+3^2+5^3+7^4.....n terms
n=int(input("Enter n number of terms : "))
c=1
sum=0
for i in range(1,n+1):
    print(c,"^",i,end=" + ")      
    sum+=c**i             
    c=c+2           
print("\b\b=",sum)

