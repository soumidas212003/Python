#1-3+5-7+9..................N terms
"""r=int(input("Enter the range: "))
c=1
s=0
for i in range(1,r+1):
    if i%2!=0:
        print(c,end="-")
        s+=c
        c+=2
    else:
        print(c,end="+")
        s-=c
        c+=2
print("\b=",s)"""

#x^1/1! - x^2/3! + x^3/5! .......n terms
#1+11+111+1111+.... upto N terms
#[0  1  1  2  3  5  8  13  21 ..... ]#Fibonacci Series...