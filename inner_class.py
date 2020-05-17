class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=6
        def show(self):
            print(self.brand, self.cpu, self.ram)
            

s1=student('navin',7)
s2=student('jony',6)
s1.show()

lap1=s1.lap
lap2=s2.lap
print(id(lap1))
print(id(lap2))

