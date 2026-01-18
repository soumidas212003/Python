def is_fibonacci_number(n):
    if n < 0:
        return False 
    a, b = 0, 1
    while a < n:
        a, b = b, a + b  
    return a == n 
number = int(input("Enter a number: "))
if is_fibonacci_number(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is not a Fibonacci number.")
