import string
Sen=input("Enter any sentence :")
v=c=d=p=0
for i in Sen:
    i=i.upper()
    if i in 'AEIOU':
        v+=1
    elif i in string.ascii_letters:
        c+=1
    elif i in string.digits:
        d+=1
    elif i in string.punctuation:
        p+=1
print(f"Vowels are : {v}\nConsonents are : {c}\nDigits are : {d}\nPunctuation are : {p}")