a= [1, 342, 75, 23, 98]
b= [75, 23, 98, 12, 78, 10, 1]
i=0
k=[]
while i<len(a):
    if a[i] in b:
        k.append(a[i])
    i+=1
print(k)
   
