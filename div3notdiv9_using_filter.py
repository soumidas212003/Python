def div3(i):
    if i%3==0 and i%9!=0:
        return i
#div3=lambda i:i%3==0 and i%9!=0
n=int(input("Enter the range: "))
num=[]
for i in range(n):
    x=int(input("Enter the number : "))
    num.append(x)
print(num)
num_list=list(filter(div3,num))
print(num_list)