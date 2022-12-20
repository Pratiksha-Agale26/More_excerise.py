# a=[1,2,3,4,5]
# b=[2,3,0,5,1]
a=[1, 5, 10, 12, 16, 20]
b=[1, 2, 10, 13, 16]
i=0
k=[]
while i<len(a):
    if a[i] not in b:
    
        k.append(a[i])
    i+=1
print(k)

