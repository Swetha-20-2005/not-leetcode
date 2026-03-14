a=["hii hello welcome back to my channel","swetha is agood girl","abarna is beautiful girl"]
b=[]
c=[]
for i in range(len(a)):
    if(i%2==0):
        b.append(a[i].split())
for i in range(len(b)):        
    for j in range(len(b[i])):
        if(j%2==0):
            c.append(b[i][j][::-1])
        else:
            c.append(b[i][j])
print(c)        
        

OUTPUT:
print the odd number la irukara string fulla even number numbers la irukara words ah reverse change pannanum     
        
                   
        
            
            
