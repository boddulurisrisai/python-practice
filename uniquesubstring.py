s=input('enter string')
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if len(s[i:j])>1:
            l.append(s[i:j])
l.sort()
print(l)
