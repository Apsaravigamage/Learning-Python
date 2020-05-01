#Tuple & set   tuple cant chance the value
tup=(21,67,56,45,43)
print(tup)

#set collection of uniq elements
s={22,24,36,5,65}
#print(s[2]) set index are not valid
s.remove(22)
print(s)

num=5
print(id(num))#address of num

a=10
b=a
print(a)
print(b)
print(id(a))
print(id(b))#a & b have a same id because python multiple variabls have same value dont use multipul data

#data typy

# (none(null),
# numeric(int,float,complex,bool),
nums=9.8
print(type(nums))
nums=4
print(type(nums))
nums=6+4j
print(type(nums))
a=5.6
b=int(a)
print(type(b))
print(b)

k=float(b)
print(k)

k=6
c=complex(b,k)
print(c)

print(b>k)
print(int(True))
print(int(False))

# Sequence(list,tuple,set,string,range,)
lst=[1,2,3,4]
print(type(lst))

s={23,4,5,6}
print(type(s))

t=(3,5,7,8)
print(type(t))

str='Apsara'#python havent characer

print(range(10))
print(list(range(10)))
print(list(range(2,10,2)))#first is 2 last is 10 difference is 2
print(type(range(10)))

# dictionary every value lest assing a key

d={'Apsara':'Cat','Nawo':'Dog','Hima':'Puppy'}
print(d)
print(d.keys())
print(d.values())
print(d['Nawo'])

#operators
# Arithmetic
x=5
y=4
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#Assignment
x=x+2
print(x)
x+=2
print(x)
x-=2
print(x)
x*=2
print(x)
x/=2
print(x)

a,b=5,8
print(a)
print(b)

#Relational
print(a<b)
print(a>b)
print(a==b)
a=8
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
b=6
print(a!=b)

#Logical (and or not )
a=3
b=9
print(a<8 and b<3)
print(a<8 or b<3)
x=True
print(x)
print(not x)


#Unary
n=4
print(n)
print(-n)

