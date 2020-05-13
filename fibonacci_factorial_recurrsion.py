def fib(n): # fibonacci sequence
    a=0
    b=1
    if n==1:
        print(a)
    else:
         print(a)
         print(b)

         for i in range(2,n):
            c=a+b # swap
            a=b
            b=c
            print(c)
x=int (input("Enter your num"))
fib(x)


def fact(n):#Factorial of number
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=int(input("your num"))
result = fact(x)
print(result)

#import sys #Recursion
#sys.setrecursionlimit(2000)
#print(sys.getrecursionlimit())
#i=0
#def greet():
    #global i
    #i+=1
    #print("Hello",i)
    #greet()
#greet()

def fact(n):#factorial using recursion
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(5)
print(result)

