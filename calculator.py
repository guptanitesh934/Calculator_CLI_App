print("=====Welcome to Calculator CLI App=====","\n")

# Taking input & choice from user
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
print("\n")
x=input("Enter the Mathematical Operator:")
print("\n")

if x=="+":
    print(a,"+",b,"=",a+b)

elif x=="-":
    print(a,"-",b,"=",a-b)

elif x=="/":
    if b==0:
        print("Error! Division by zero is not allowed")
    else:
        print(a,"/",b,"=",a/b)

elif x=="*":
    print(a,"*",b,"=",a*b)

else:
    print("No match found ! Please Enter Valid Input")


