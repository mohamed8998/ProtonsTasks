operator=input("enter an operator(+,-,*,/,%): ")
x=float(input("enter first number: "))
y=float(input("enter second number: "))
if operator== "+":
    result= x + y
    print(result)
elif operator== "-":
    result= x - y
    print(result)
elif operator=="*":
    result= x * y
    print(result)
elif operator=="/":
    result= x / y
    print(result)
elif operator=="%":
    result= x % y
    print(result)
else :
    print("invalid operator")