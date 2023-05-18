def fact(x):
    if x == 1:
        return 1
    elif x==0:
        return 1
    else:
        return x * fact(x-1)

def last4(str):
    return str[-4:]
a=int(input())

print(last4(str(fact(a))))
