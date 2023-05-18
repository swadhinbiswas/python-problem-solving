n=int(input())
s1=[]

for i in range(n):
    s1.append(input())
    i=i+1


def test(y):
    count=0
    for j in range(len(y)):
        if y[j].isdigit():
            return count+1
        j=j+1
        
def countBall(s1):
    k=0 
    y=s1[k]
    for k in range(n):
        if test(y)==6:
            print("1 OVER")
        if test(y) == 6:
            print(test(y),"BALLS")
        k=k+1
        
        


countBall(s1)