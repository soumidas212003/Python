dict={}
roll=int(input("Enter any number : "))
dict[roll]={}
name=input("Enter any name : ")
dept=input("Enter department name : ")
T_marks=int(input("Enter total marks : "))
dict[roll]['Name']=name
dict[roll]['Department']=dept
dict[roll]['Total marks']=T_marks
print(dict)