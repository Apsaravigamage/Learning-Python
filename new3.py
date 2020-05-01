#Number System convertion in python
# Binary
# Decimal
# octal
# Hexa Decimal = mac address ,IPv6

print(bin(25))# Decimal -> Binary
print(0b0101) # Binary -> Decimal
print(oct(25))#Decimal -> octal
print(hex(25))#Decimal -> Hexa
print(hex(10))
print(0xf)

#Swap 2 variable in python
a=5
b=6
#temp=a
#b=temp
#print(a)
#print(b)

a=a^b #11 use XOR
b=a^b #5
a=a^b #6

print(a)
print(b)

a,b=b,a
print(a)
print(b)








