###Errors

# - Syntax Error or Compile Error
## Logical Error
## - Run Time Error

##Run Time Error  - Exception

a=5
b=1

try:
    print("Resource open")
    print (a/b)
    k= int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You can't Divide a number by zero")

except ValueError as e:
    print ("invalid Input")

except Exception as e:
    print ("Something went wrong")

finally:
    print("Resource close")

print ("Hai")