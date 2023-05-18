y=int(input())

count=0
for i in range(1,y+1):
    if y%i==0:
        count+=1
    i=i+1
print(count-1)
    