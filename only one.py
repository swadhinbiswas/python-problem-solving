m,n= map(int,input().split())
l=[list(map(int,input().split(' '))) for i in range(m)]
for i in range(int(input())):
    r,c=map(int,input().split())
    l[r-1][c-1],l[r-1][c],l[r-1][c+1],l[r][c+1],l[r+1][c+1],l[r+1][c],l[r+1][c-1],l[r][c-1]=l[r][c-1],l[r-1][c-1],l[r-1][c],l[r-1][c+1],l[r][c+1],l[r+1][c+1],l[r+1][c],l[r+1][c-1]
    for x in l:
        for y in x:
            print(y,end=" ")
        print()