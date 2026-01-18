def div2(i):
    if i%2==0:
        return i
    else:
        return "Flase"
n=int(input("Enter the range : "))
num=[]
for i in range(n):
    x=int(input("Enter a number: "))
    num.append(x)
print(num)
num_list=list(map(div2,num))
print(num_list)