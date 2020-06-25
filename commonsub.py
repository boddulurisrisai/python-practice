x=input('enter str1')
y=input('enter str2')
a=[]
b=[];c=[];max=-1
for i in range(len(x)+1):
    for j in range(i+1,len(x)+1):
        a.append(x[i:j])
for i in range(len(y)+1):
    for j in range(i+1,len(y)+1):
        b.append(y[i:j])
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            if len(a[i])>max:
                max=len(a[i])
                c=a[i]
print(c)
        
