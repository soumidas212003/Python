def binarysearch(mylist,key):
    low=0
    high=len(mylist)-1
    while(low<=high):
        mid=(low+high)//2
        if key==mylist[mid]:
            return mid
        elif key<mylist[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
n=int(input("Enter the range: "))
list=[]
for i in range(n):
    x=int(input("Enter the number: "))
    list.append(x)
list.sort()
print("Sorted list: ",list)
key=int(input("Enter the number to search: "))
index=binarysearch(list,key)
if index != -1:
    print("Found")
else:
    print("Not found")