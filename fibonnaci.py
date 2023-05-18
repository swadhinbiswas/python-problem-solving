def fibonnachi(n):
    if n == 0 :
        return 0
    if n==1:
        return 1
    return fibonnachi(n-1) + fibonnachi(n-2)

x,y=map(int,input().split())
setp=[]
for i in range(x,y+1):
    if fibonnachi(i)<y+1:
        setp.append(fibonnachi(i))
    else:
      break
  
print(set(setp))
