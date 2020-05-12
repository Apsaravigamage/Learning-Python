a=10 # global variable
print(id(a))
def some ():
    a=12 # local variable

    x=globals()['a']
    print(id(x))
    print("in fun",a)
    globals()['a']=3 #change globle value
some()
print("outside",a)

# pass list to a function
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst =[12,34,57,43,56,45,90]
even, odd = count(lst)
print("Even :{} and odd :{}".format(even,odd))
