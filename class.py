class computer: #class
    # class have two things attribute(variable) & behaviour(methods,function)

    def __init__(self, cpu, ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):# here it is method
        print("config is",self.cpu,self.ram)

x=5 #int built class
print(type(x))

a='3'
print(type(a))

com1 =computer('we', 3)#object of computer constructor
com2=computer('3', 6)
print(type(com1))
 #main is moduler
#computer.config(com1)# if we want use method config pass object com1
com1.config() #pass variable it self
com2.config()

