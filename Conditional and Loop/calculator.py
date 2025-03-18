a = float(input("Enter the first operand = "))
b = float(input("Enter the second operand = "))
c = input("Enter the operator = ")
if c == "+":
    print(a,"+",b," is ",a+b)
elif c == "-":
    print(a,"-",b," is ",a-b)
elif c == "*":
    print(a,"*",b," is ",a*b)
elif c == '/':
    print(a,"/",b," is ",a/b)
else:
    print("Enter valid operator")