def bigger_number(s):
    big=s[0]
    for i in range(len(s)):
        if s[i]>big:
            big=s[i]
            i=i+1
    return big
def count(s):
    count=0
    for i in range(len(s)):
        if s[i]==bigger_number(s):
            count=count+1
    return count

    