from numpy import *
arr=array([1,2,3,4,5.0])
print(arr.dtype)
print(arr)
#array using different function
#linspace()
arr=linspace(0,15,16)#0 to 15 in 16 different parts
print(arr)

#logspace()
arr=logspace(1,40,5)
print('%.2f'%arr[1])

#arange()
all= arange(1,15,2)#1 to 15 skip 2 elements
print(all)

#zeros()
arr=zeros(5)
print(arr)

#ones()
arr=ones(5)
print(arr)

#copying an array
arr=array([1,2,3,4,5])# add the value each element
arr=arr+5
print(arr)

# add 2 different array
arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])
arr3=arr1+arr2
print(arr3) # vectorized operation

arr1=array([1,3,5,7])
print(sin(arr1)) #sin values in array
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))
print(concatenate([arr1,arr2]))

arr1=array([6,7,8,9])
arr2=arr1
print(arr1)
print(arr2)
print(id(arr1)) # aliasing
print(id(arr2))

arr1=array([6,7,8,9])
arr2=arr1.view()# view is a function to creat a new array in different location
print(arr1)
print(arr2)
print(id(arr1))# the address is different
print(id(arr2))

# shallowcopy the values are changing both arrays
arr1=array([6,7,8,9])
arr2=arr1.view()
arr1[1]=3
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

# deepcopy havent link another array use copy function
arr1=array([6,7,8,9])
arr2=arr1.copy()
arr1[1]=3
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

