#parameterized Constractor
class person:
    def __init__(self,n,o):
        self.name=n
        self.occ=o
        print("I am a person")
    def info(self):
        print(self.name,"is a",self.occ)  
a=person("Soumita","Developer")
a.info()
b=person("Ruban","HR")
b.info()