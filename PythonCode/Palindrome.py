# WAP to check weather a number palindrome or not
n=int(input("Enter a number : "))
s=0
temp=n
while(n>0):
    r=n%10              #1      5       1
    s=(s*10)+r          #1      15      151
    n=n//10             #15     1       0
if temp==s:
    print("Palindrome number ")
else:
    print("Not a palindrome number ")