x=int(input())
ordable=input()
chardata=[]
for i in range(len(ordable)):
      x=ord(ordable[i])
      chardata.append(x)
      i=i+1
for i in range(len(chardata)):
      if chardata[i]==' ':
            chardata[i]=''
      else:
            chardata[i]=chr(ord(chardata[i])-x)
            i=i+1
print(''.join(chardata))