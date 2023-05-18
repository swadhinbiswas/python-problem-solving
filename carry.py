
def carry(a,b):
    a1=[0]*10
    b1=[0]*10
    i=0
    while (a!=0 and b!=0):
        if (a!=0):
           a1[i]=a%10
           a=a//10
           return a1
        
        if (b!=0):
           b1[i]=(b%10)
           b=b//10
           return b1
def final(a1,b1):
    


        
        
        
x,y=map(int,input().split())
a1=carry(x,y)
b1=carry(x,y)
c=final(a1,b1)

if c==1:
    print("Yes")
else:
    print("No")

            


    
        
        
           
    