#Write a program in python to find the largest difference between the elements of a list.
list=[]
Range=int(input("Enter The Range : "))
for i in range(Range):
    x=int(input("Enter a number you want to insert : "))
    list.append(x)
for i in range(Range):
    print(list[i],end =" ")
Max=list[0]
Min=list[0]
for i in range(Range):
    if list[i]>Max:
        Max=list[i]
    if list[i]<Min:
        Min=list[i]
print("The largest difference between the elements of a list :",Max,"-",Min,"=",(Max-Min))