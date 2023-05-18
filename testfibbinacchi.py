a=[0,1,2]
while len(a)<41:
    a+=[sum(a[-2:])]
x,y=map(int,input().split())
[print(i)for i in a if x<=i<=y]