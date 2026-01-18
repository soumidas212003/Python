def linearsearch(mylist,key):
    n=len(mylist)
    found=False
    for i in range(n):
        if key == mylist[i]:
            found=True
            break
    if found:
        print("Found")
    else:
        print("Not Found")
n=int(input("Enter the range: "))
list=[]
for i in range(n):
    x=int(input("Enter the number: "))
    list.append(x)
print("Sorted list: ",list)
key=int(input("Enter the number to search: "))
linearsearch(list,key)
