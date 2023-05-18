x,y=map(int,input().split())


temp=y
while(temp%x!=0):
    temp+=1
    
    
print(temp-y)