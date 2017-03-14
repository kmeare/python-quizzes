l1 = [0, 1]
ending = 100

for i in range(0, ending-1):
    l1.append(l1[len(l1)-1] + l1[len(l1)-2]) 

print (l1) 


