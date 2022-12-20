a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print(a,"a greater")
elif b>a and b>c:
    print(b,"b greater")
elif c>a and c>b:
    print(c,"c greater")
else:
    print("none")