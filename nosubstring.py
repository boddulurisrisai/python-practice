str=input('enter string')
s=str.split(',')
a=s[0];count=0
b=s[1]
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        a1=a[i:j]
        if not b in a1:
            count+=1
print(count)
    
