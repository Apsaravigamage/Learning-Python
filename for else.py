nums=[12,34,23,17 ] #only first num divisible by 5
for num in nums:
    if num%5==0: # condition
        print(num)
        break # use to come out to the loop
else:
     print("not found")

# find a given number is prime or not
num=10
for i in range(2,num):
    if num %i==0:
        print("not prime")
        break
else:
    print("prime")