# 1
# 3 5
# 5 7 9
# 7 9 11 13 
n=int(input("Enter n number:"))
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=2
    print()    