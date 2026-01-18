def pow(base,exp):
    if exp != 0:
        return base * pow(base,exp-1)
    else:
        return 1
base=int(input("Enter base: "))
exp=int(input("Enter exponent: "))
print(pow(base,exp))