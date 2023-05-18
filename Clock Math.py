import math
def timei(h,m):
    return (h*30+(m/60)*30)-(m*6)
h,m=map(int,input().split())
t=timei(h,m,)
if t<0:
    t=t*-1
    print("{:.8f}".format(t))
if t>180:
    t=360-t
print("{:.8f}".format(t))
    