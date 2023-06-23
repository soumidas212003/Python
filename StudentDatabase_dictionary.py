def input_dict(dict):
    s_roll=int(input("Enter student roll : "))
    dict[s_roll]={}
    s_name=input("Enter any name : ")
    s_dept=input("Enter department name : ")
    s_sub=int(input("Enter how many subjects are student have : "))
    sum=0
    for i in range(1,s_sub+1):
        sub_name=input(f"Enter sub {i} name: ")
        sub_marks=int(input(f"Enter {sub_name} marks : "))
        sum+=sub_marks
        dict[s_roll]['Student name']=s_name
        dict[s_roll]['Department name']=s_dept
        dict[s_roll][sub_name]=sub_marks
    dict[s_roll]['Total marks']=sum
    dict[s_roll]['Average']=sum/s_sub
def display(dict):      
    print(dict)
def search(s_roll,dict):
    print(dict[s_roll])
dict={}
while 1:
    print("Enter 1 to input into the dictionary: ")
    print("Enter 2 to display from the dictionary: ")
    print("Enter 3 to search from the dictionary: ")
    choice=int(input("Enter your choice : "))
    if choice==1:
        input_dict(dict)
    elif choice==2:
        display(dict)
    elif choice==3:
        roll=int(input("Enter the roll you want search: "))
        search(roll,dict)
    else:
        break
