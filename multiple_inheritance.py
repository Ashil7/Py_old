class First:
    def display(self):
        print("first")
class Second:
    def display(self):
        print("second")
class Third(Second,First):
    def display3(self):
        print("Third")


x=Third()
x.display3()
x.display() #calls first display according to the inheritance

print(Third.mro())