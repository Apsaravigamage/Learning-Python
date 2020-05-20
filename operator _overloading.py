a=4
b=9
print(a+b)
print(int.__add__(a,b)) #add method

a=24
b=9
print(a-b)
print(int.__sub__(a,b)) # sub method



class student:   # operator overloading
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1= self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self, other):#grater than method of s1>s2
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self): # method of print(s1)
        return '{} {} '.format(self.m1,self.m2)


s1=student(56,78)
s2=student(90,34)

s3=s1+s2

if s1>s2:
    print("s1 win")
else:
    print("s2 win")

a=6
print(a.__str__())
print(s1)
print(s2)