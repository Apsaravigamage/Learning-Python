class computer:
    pass

c1=computer()
c2=computer()

print(id(c1))
print(id(c2))

class comput:
    wheels=4 # class variable
    def __init__(self):
        self.name="navin" #instance variable because values are change
        self.age=20 #instance variable inside of init
    def update(self):
        self.age=28
c1=comput()
c2=comput()

if c1==c2:
    print("same age")
else:
    print("different")
c1.update()

c1.name="green"
c1.age=12

print(c1.name)
print(c2.name)