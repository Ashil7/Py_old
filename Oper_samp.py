#Operator Overloading

class Sample:
    def set_name(self,name):
        self.name=name

    def __add__(self, other):
        name=self.name+" "+other.name
        return name

first_name=Sample()
second_name=Sample()

first_name.set_name("Ashil")
second_name.set_name("Benny")

full_name=first_name+second_name
print(full_name)