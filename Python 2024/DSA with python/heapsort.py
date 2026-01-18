def heapify(list,n,i):
    largest=i
    left=2*i
    right=2*i+1
    if left < n and list[left] > list[largest]:
        largest=left
    if right < n and list[right] > list[largest]:
        largest=right
    if largest != i:
        list[i],list[largest]=list[largest],list[i]
        heapify(list,n,largest)
def heapsort(list):
    n=len(list)-1
    i=n//2
    while i>0:
        heapify(list,n,i)
        i-=1
    i=n
    while i>0:
        list[1],list[i]=list[i],list[1]
        heapify(list,i,1)
        i-=1
n=int(input("Enter the size: "))
list=[]
for i in range(n):
    ele=int(input("Enter the number: "))
    list.append(ele)
print(list)
heapsort(list)
print(list)