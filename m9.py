def harshad():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    i=0
    sum=0
    n=a
    while a>b:
        i=a%10
        sum=sum+i
        a//=10
    
    if n%sum==0:
        print(True,"Harshad number")
    else:
        print(False,"Not")

harshad()


# i=1
# while i<=100:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print("p",i)
#     else:
#         print("not",i)
#     i+=1


# def digitsSum(Number):
#     Sum = rem = 0
#     while Number > 0:
#         rem = Number % 10
#         Sum = Sum + rem
#         Number = Number // 10
#     return Sum

# minHrd = int(input("Enter the Minimum Harshad Number = "))
# maxHrd = int(input("Enter the Maximum Harshad Number = "))

# print("\nThe List of Harshad Numbers from {0} and {1}".format(minHrd, maxHrd)) 
# for i in range(minHrd, maxHrd + 1):
#     Sum = digitsSum(i)
#     if i % Sum == 0:
#         print(i, end = '   ')