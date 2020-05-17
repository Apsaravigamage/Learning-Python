class A: # Super Class
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 working ")
    def feature2(self):
        print("feature 2 working ")

class B (A): #sub Class  single level inheritance
    def __init__(self):# then run B init  constructor in inheritons
        super().__init__() #  first run init of A
        print("in A init")
    def feature3(self):
        print("feature 3 working ")
    def feature4(self):
        print("feature 4 working ")

class C(B):# multi level inheritance
    def feature5(self):
        print("feature 5 working ")

a1= A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature1()

c1=C()
c1.feature4()

