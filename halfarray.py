a=[1,2,5,3,11,12]
slow=0
fast=0
while(fast<len(a) and fast+1<len(a)):
    slow+=1
    fast+=2
print(a[:slow+1])

OUTPUT:
[1,2,5,3]
