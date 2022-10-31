class BaseClass:
    def __init__(self):
        print("Base init")
    def set_name(self,name):
        self.name=name
        print("base setname")

class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("Sub init")
    def set_name(self,name):
        super().set_name(name)
        print("sub setname")


    def welcome(self):
        print("Welcome")
    def display(self):
        print("Name :"+self.name)


y=SubClass()
y.welcome()
y.set_name("Ashil")
y.display()
