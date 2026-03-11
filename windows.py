arr=[15,8,25,4,12,6]
k=4
currentmax=0
for i in range(0,len(arr)-k+1):
    s=sum(arr[i:i+k])
    currentmax=max(currentmax,s)
print(currentmax)
