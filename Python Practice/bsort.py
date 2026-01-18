def bsort(mylist):
    n=len(mylist)
    for i in range(n-1):
        flag=False
        for j in range(n-1-i):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
                flag=True
        if flag==False:
            break
    return list
n=int(input("Enter the range: "))
list=[]
for i in range(n):
    x=int(input("Enter the number: "))
    list.append(x)
print("Before sort: ",list)
print("After sort: ",bsort(list))