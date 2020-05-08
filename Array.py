# all the value of same type
# dont have fix size in python

from array import * # * means all function
vals=array('i',[5,6,-78,8,9,4])# 'i'integer array we can use negative values
print(vals)

min=array('I',[5,6,78,8,9,4])# 'I'is unsigned int
print(min)

print(vals.buffer_info())# size of the array address &size

print(vals.typecode) # i

vals.reverse()
print(vals)

print(vals[2]) #index

for i in range(len(vals)):
    print(vals[i])

bro=array('u',['a','r','t'])
for e in bro:
    print(e)

vals=array('i',[5,6,7,8,9])# assign new array
newArr=array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e)

i=0 # do same thing above
while i<len (newArr):
    print(newArr[i])
    i+=1


# inserting / searching elements in Array

arr=array('i',[])
n = int(input("Enter the Length of Array"))
for i in range(n):
    x= int(input("Enter the next num"))
    arr.append(x) # add valus to the array
print(arr)


val= int(input("Enter the value for search"))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1

print(arr.index(val)) # above loop function
