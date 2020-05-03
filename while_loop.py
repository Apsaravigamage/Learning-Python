i=1  #Initialization
while i<=5: #Condition
    print("cat")
    i=i+1 #Increment/Decrement

#multipul while
i=1
while i<=5:
    print("happy",end="")#end="" dont wont to new line
    j=1
    while j<=4:
        print("cat",end="") #innerloop and go back to the outerloop
        j=j+1
    i=i+1
    print()# print give a newline

i=1
while i<=4:
    print("#", end="")
    j=1
    while j<=5:
        print("#", end="")
        j=j+1
    i=i+1
    print()


