#Write a program in python to spilt a list into odd and even two different list.
list=[]
Odd=[]
Even=[]
Range=int(input("Enter the range : "))
for i in range(Range):
    x=int(input("Enter the number you want to insert : "))
    list.append(x)
for i in range(Range):
    if list[i]%2==0:
        Even.append(list[i])
    else:
        Odd.append(list[i])
print("The Original list is : ",list)
print("The Even list is : ",Even)     
print("The Odd list is : ",Odd)   