#all recursive function is here
def pow(base,exp):
    if exp==0:
        return 1
    x=pow(base,exp-1)
    y=base*x
    return y