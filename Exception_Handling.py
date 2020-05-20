a=int(input("enter 1num"))
b=int(input("enter 2num"))

try:
    print("resource open")
    print(a/b)

    k=int(input("Enter num"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e: # only run we get error
    print("Something went Wrong...")

finally:
    print("resource closed")
print("bye")