#Soumita Das
#S.Das
import string
name=input("Enter a string : ").split()
new_name=[]
print("print original name : ")
for i in name:
    print(i,end=" ")
print("\nAbbreviated name : ")
for x in name:
    new_name.append(x[0].upper())
new_name.remove(new_name[-1])
for i in new_name:
    print(i,end=".")
print(name[-1].title())