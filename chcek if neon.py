n=int(input())
b=n*n
sum=0
while(b!=0):
    sum+=b%10
    b//=10
if(sum==n):
    print("neon number");
else:
    print("not")


OUTPUT:
9
9*9=81-->8+1=9
9==9
neon number
