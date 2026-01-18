n=int(input("Enter a range: "))
list=[]
for i in range(n):
    x=int(input("Enter a number : "))
    list.append(x)
print(list)
for i in range(n):
    print(list[i],end=" ")