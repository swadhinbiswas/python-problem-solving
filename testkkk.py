n=int(input())
a=[]
sum=0
avg=0
j=1
for j in range(n):
     a.append(int(input()))
     
     
for i in range(1,n+1):
        sum=sum+a[i-1]
        avg = sum/i
        print("%.5f\n" %avg)
        i=i+1
