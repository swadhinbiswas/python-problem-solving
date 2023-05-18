a=input().lower()
b=input().lower()
if (len(a)==len(b)):
    if(sorted(a)==sorted(b)):
        print("Yes")
    else:
        print("No")