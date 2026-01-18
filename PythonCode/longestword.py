# Techno India Hoogly
# Hoogly and 7
sentence=input("Enter any sentence : ").split()
max=0
for x in sentence:
    if len(x)>max:
        max=len(x)
        name=x
print(f"The longest lenth is {max} and the word is {name}")