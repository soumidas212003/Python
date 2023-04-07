import functools
add=lambda a,b:a+b
n=int(input("Enter the range : "))
list=[]
for i in range(n):
    x=int(input("Enter the number : "))
    list.append(x)
for i in range(n):
    print(list[i],end=" ")
sum=functools.reduce(add,list)
print("\n",sum)
