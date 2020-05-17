class student:
    school='Telusko' # class variable
    def __init__(self,m1,m2,m3):
        self.m1=m1 # instance variable
        self.m2=m2
        self.m3=m3

    def avg(self): #instance method because work with object
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):#
        return self.m1
    def set_m1(self,value):
        self.m1=value

    @classmethod
    def getschool(cls):#class method
        return cls.school
    @staticmethod
    def info():
        print("This is the student class")


s1=student(23,45,67)
s2=student(46,90,78)

print(s1.avg())
print(s2.avg())

print(student.getschool())

student.info()