def topten():
     yield 5 # keyword make our function as a generator
     yield 4
     yield 3
     yield 2
     yield 1
values= topten()
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

def TopTen():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
values=TopTen()

for i in values:
    print(i)

