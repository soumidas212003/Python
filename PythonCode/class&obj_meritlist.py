class student:
    def __init__(self,name,roll,total_marks):
        self.name=name
        self.roll=roll
        self.total_marks=total_marks
    def display(self):
        print("\n")
        print(f"student name : {self.name}")
        print(f"student roll : {self.roll}")
        print(f"student total marks : {self.total_marks}")
        print("\n")
list=[]
n=int(input("How many students: "))
for i in range(n):
    name=input(f"Enter the name of student {i+1}: ")
    roll=int(input(f"Enter the  roll of {name}: "))
    total_marks=int(input(f"Enter the total marks of {name}'s: "))
    list.append(student(name,roll,total_marks))
list.sort(key=lambda s:s.total_marks,reverse= True)
for i in list:       
    i.display()