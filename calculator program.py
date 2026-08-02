a=int(input("enter a:"))
b=int(input("enter b:"))
operator=input("enter operator(+,-,*,/,**):")
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
elif operator=="**":
    print(a**b)
else:
    print("invalid operator")
    