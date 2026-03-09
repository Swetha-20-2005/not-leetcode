a=input()
low=[]
upp=[]
num=[]
spl=[]
for i in a:
    if('a'<= i <= 'z'):
        low+=i
    elif('A'<= i <='Z'):
        upp+=i
    elif('0' <= i <='9'):
        num+=i
    else:
        spl+=i
print("".join(low))
print("".join(upp))
print("".join(num))
print("".join(spl))
       
OUTPUT:
i/p:Swetha@2005$
wetha
S
2005
@$
