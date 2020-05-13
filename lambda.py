f=lambda a:a*a #lambda Anonymous Function who function without function name
result=f(4)
print(result)

f=lambda a,b:a+b
result=f(3,5)
print(result)

#def is_even (n):
    #return n%2==0   don"t want this function we can use lambda
nums=[9,3,4,5,6,7,8]
evens=list(filter(lambda n:n%2==0,nums))#filter()
print(evens)


nums=[9,3,4,5,6,7,8]
doubles=list(map(lambda n:n*2,evens))#map()
print(doubles)


from functools import reduce

sum = reduce(lambda a,b:a+b,doubles)#reduce()
print(sum)

