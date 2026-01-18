class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"my name is {self.name} and my age is {self.age}")
na=input("Enter your name : ")
ag=int(input("Enter your age : "))
a=person(na,ag)
a.display()
b=person("Ruban",20)
b.display()