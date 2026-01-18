#26. Write a function to count the number of words in a string.
def CountWords(name):
 return len(name.split())
 
name=input("Enter the string:- ") 
print(CountWords(name))