def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks")
    return mfx
@greet
def hello():
    print("Hello Everyone...")
@greet
def add(a,b,c):
    print(a+b+c)
hello()
add(4,5,1)