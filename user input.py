#how to get user input
# we have to use input function
x=input("Enter 1st Number")
a=int(x) #x Str is convert to int
y=input("Enter 2nd Number")
b=int(y)
z=a+b
print(z)

#above we waste line
x=int(input("Enter 1st Number"))
y=int(input("Enter 2nd Number"))
z=x+y
print(z)

#input a character
ch =input('Enter a char')#[0]
print(ch[0])# user give us to string we can get only character

# we can evaluate user expretion
result=eval(input('Enter an expr'))
print(result)
