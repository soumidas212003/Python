n=int(input("Enter the length of the list: "))
list=[]
for i in range(n):
    element=input(f"Enter the element {i+1}: ")
    list.append(element)
print("List elements are: ",list)
uni=[]
dup=[]
for i in list:
    if i not in uni:
        uni.append(i)
    else:
        if i not in dup:
            dup.append(i)
if dup:
    print("Duplicate elements are: ",dup)
else:
    print("No duplicate elements found.")