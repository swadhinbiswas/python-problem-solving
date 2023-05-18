n=int(input())
a=[]
sum=0
avg=0

for j in range(1,n):
     a.append(int(input()))
     sum=sum+a[j]
     avg = sum/j
     print("%.5f\n" %avg)
     j=j+1