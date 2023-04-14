n=int(input("Enter the range: "))
list=[]
for i in range(n):
    x=input("Enter the name: ")
    list.append(x)
name=input("Enter word you want to join: ")
li=name.join(list)
print(li)