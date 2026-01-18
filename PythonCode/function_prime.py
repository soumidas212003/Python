def prime(n):
    for i in range(2,n//2): # 2,3,4,5,6
        if n%i == 0:        # 7
            print("Not Prime")
            break
    else:
        print("Prime Number")
n=int(input("Enter the number : "))
prime(n)