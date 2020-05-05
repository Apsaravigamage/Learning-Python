print(5+3)
print(5-3)
print(5/2)
print(5*2)
print(5//2)#integer Division
print(8+4-2)#()/*+-
print(5**2)#power of
print(5%2)#moduler

print('apsara')
print("Apsra's laptop")
print('apsara"laptop"')
print('apsara\'s')#\ tells ' has special meaning
print(10*'Apsara')
print(r'c:\docs\Apsara')#raw string (r)= dont try to convert special character

# Variable
x=2
y=5
print(x+3)
print(x+y)
x=9
print(x)
print(x+10)

name='Apsara'
print(name)
print(name +' Gamage')
print(name[0])#01234
print(name[5])
print(name[-1])
print(name[0:3])
print(name[:4])
print(name[3])
print('Hi '+ name[0:4])

myname='Himasha'
print(len(myname)) # 1234

#list
nums=[2,30,55,34,12,80]
print(nums)
print(nums[0])
print(nums[2:4])
print(nums[-1])

names=['Apsara','Hima','Gamage']#list of string
print(names)

values=[4.5,'Apsara',79] #list with different data

nums.append(45)
print(nums)

nums.insert(3,7)
print(nums) 

nums.remove(55)
print(nums)

nums.pop(0)
print(nums)

del nums[2:]
print(nums)

nums.extend([29,6,97])
print(nums)

print(min(nums))

print(max(nums))

print(sum(nums))

nums.sort()
print(nums)
