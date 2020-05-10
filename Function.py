def greet(): # define function
    print ("hello")
greet() # call function
greet()

def add (x,y):
    c=x+y
    print(c)
add(2,3)

def add (x,y): #function can return or not values
    c=x+y
    return c
result=add(8,3)
print(result)

def add_sub (x,y):# one function return multiple values
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(6,3)
print(result1,result2)

def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x",x)
a=10
print(id(a))
update(a)
print("a",a)
#python dont use pass by value/pass by reference


#Types of Arguments
def add(a,b): # formalargument
    c=a+b
    print(c)
add(6,4)#Actual arguments
#Types of Actual Arguments (position/ keyword/ default/ variable length)
def person (name,age):
    print(name)
    print(age)
person (name='Kamal',age=28) #keyword

def person (name,age=18):#default
    print(name)
    print(age)
person ('Kamal')

def sum (a,*b):# * =we have multipul value
    c=a
    for i in b:
        c=c+i
    print(c)
sum(5,7,4,3)# variable length

def person(name,**data): # keyworded variable length argument
    print(name)
    for i,j in data.items(): #print one by one data
        print(i,j)

person('Kamal',age=23,country='SriLanaka',mob=789453)
