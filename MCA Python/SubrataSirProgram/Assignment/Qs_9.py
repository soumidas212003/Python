num = int(input("Enter any number: "))
for i in range(2, num + 1):
    f = 0
    if num % i == 0:
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                f = 1
                break
        if f == 0:
            print(f"Prime factor: {i}")
