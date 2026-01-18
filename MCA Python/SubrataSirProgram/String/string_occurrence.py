#24. Write a program to count the occurrence of each word in a string.
str=input("Enter a string: ").split()
c={}
for i in str:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)