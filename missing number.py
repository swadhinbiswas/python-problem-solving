n=int(input())
x = [int(x) for x in input().split()]
sum=0
for i in range(len(x)):
    sum=sum+x[i]
    i=i+1
print(n-sum)