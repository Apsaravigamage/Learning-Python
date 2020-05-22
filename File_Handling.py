f= open('NEW','r') #r reading
print(f.readline(), end="")
print(f.readline(3))# only print 4 characters


f2= open ('NEW2','w') #write 
f2.write("Something")