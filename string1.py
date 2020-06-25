str=input('Enter the string')
s1=[]
s1=str.split(',')
final=''
for i in s1:
    s2=i.split(':')
    a=len(s2[0])
    max=-1
    for j in s2[1]:
        if int(j)>max:
            if int(j)<=a:
                max=int(j)
    s3=s2[0]
    if max==-1:
        final+='X'
    else:
        final+=s3[max-1]
print(final)
    
