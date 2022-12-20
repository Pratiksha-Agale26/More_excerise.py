string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
i=0
b=[]
while i<len(string_list):
        k=string_list[i]
        if k not in b:
            b.append(k)
        i+=1
print(b)
