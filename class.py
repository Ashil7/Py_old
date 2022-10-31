class SampleClass:
    def hello(self,n):
        self.name=n
    def print_name(self):
        print(self.name)

x=SampleClass()
y=SampleClass()
name ="ashil"
x.hello(name)
name ="hai"
y.hello(name)

x.print_name()
y.print_name()