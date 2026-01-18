# Write a program to display all 3 digited numbers which are divisible by 3 but not divisible by 9.
for n in range(100,999+1):
    if n%3==0 and n%9!=0:
        print(n,end=" ")
        n+=1
    