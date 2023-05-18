n=int(input())

#for i in range(n-1):
  #  for j in range(i,n-1):
       # print(" ",end='')
   # for k in range(i+1):
       # print("*",end="")
   # print()


for i in range(n):
    for j in range(i):
        print(" ",end=')
    for k in range(n-i):
        print("*",end="")
    print()   
for i in range(n):
    for j in range(n+n):
        print("*",end='')
    #look
    print()
        

