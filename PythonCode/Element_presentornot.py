n=int(input("Enter a range: "))
list=[]
for i in range(n):
    x=input("Enter a number : ")
    list.append(x)
for i in range(n):
    print(list[i],end=" ")
num=input("\nEnter the element you want to check whether the element is present or not :")
for i in range(n):
    if list[i]==num:
        print("The element is present into the list")
        break
else:
    print("The element is not present into the list")