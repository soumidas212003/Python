dict={}
sen=input("Enter any sentence : ").split()
for i in sen:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
