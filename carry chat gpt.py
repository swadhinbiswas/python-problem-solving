a, b = input().split()  
carry = 0 
nocarry= False 


if len(a) < len(b):
    a = '0'*(len(b)-len(a)) + a
else:
    b = '0'*(len(a)-len(b)) + b

for i in range(len(a)-1, -1, -1):
    de_sum = int(a[i]) + int(b[i]) + carry  
    if de_sum >= 10:  
        carry = 1
        nocarry = True  
    else:
        carry = 0

if nocarry:
    print('Yes')
else:
    print('No')