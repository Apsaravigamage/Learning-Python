from numpy import *
arr=array([
            [1,2,3,5,4,2],
            [4,5,6,8,9,3]
])
print(arr.ndim)# attribute ndim num of dimension
print(arr.shape)#num of rows & colums
print(arr.size)
arr1=arr.flatten()#convert 2D to 1D
print(arr1)
arr2=arr1.reshape(2,2,3)# 3D array
print(arr2)

m=matrix(arr)
print(m)

m=matrix('1,2,3,4 ; 5,6,7,8')# dont need to array
print(m)
m=matrix('1,2,3;4,5,6;7,8,9')
print(diagonal(m))
print(m.min())
print(m.max())

m1=matrix('1,2,3;4,5,6;7,8,9')
m2=matrix('1,5,3;4,3,6;1,8,5')
m3=m1+m2;
print(m3)
m3=m1*m2;
print(m3)

