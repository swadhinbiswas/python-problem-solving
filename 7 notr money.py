a=int(input())
b=[]
for i in 500,100,50,10,5,1:
    while a-i>=0:
        b+=[i]
        a-=i
print(*sorted(b))