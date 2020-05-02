if False: # excicute the statement is only true (suite)
    print("correct")# indentation
print('bye')# dose not belong to false


x=int(input("enter num"))
r=x % 2
if r==0:
    print("Even")
    if x>5:#only chack first if is correct inside the if
        print("Great")
    else:
        print("Not Great")
else:
    print("odd")


n=int(input("Enter num"))
m=n<0
if m==0:
    print("positive")
else:
    print("negative")


a=int(input("Enter num"))
if a==1:
    print("One")
elif(a==2):
    print("Two")
elif(a==3):
    print("Three")
elif(a==4):
    print("Four")
else:
    print("Wrong Input")

