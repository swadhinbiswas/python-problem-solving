x,y=map(int,input().split())

def chess(x,y):
    try:
        if x==y:
            return 0
        elif x%2==0 and y%2==0:
            return 0
        elif x%2!=0 and y%2!=0:
            return 0
        else:
            return 1
    except ZeroDivisionError:
        if x==0 and y%2==0:
            return 0
        
        elif y==0 and x%2==0:
            return 0
        else:
            return 1
        

def blackorwhile(x, y):
    if chess(x,y)==0:
        return "black"
    elif chess(x,y)==1:
        return "white"


print(blackorwhile(x,y))
