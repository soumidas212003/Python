#Default Constractor
class person:
    name="sou"
    occ="developer"
    def __init__(self):
        print("I am a person")
    def info(self):
        print(self.name,"is a",self.occ)  
a=person()
a.info()
