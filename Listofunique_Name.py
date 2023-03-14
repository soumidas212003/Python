#Write a program in python to create a list of unique names. Program should generate appropriate message for duplicate inputs.
list=[]
n=int(input("Enter the range : "))
while n!=0:
    x=input("Enter the element: ")
    if x not in list:
        list.append(x)
    else:
        print("The element is present in the list")
        n+=1
    n-=1
print(list)