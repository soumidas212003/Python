def gcd(m,n):
    if n%m==0:
        return m
    else:
        return gcd(n%m,m)
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
print(gcd(num1,num2))