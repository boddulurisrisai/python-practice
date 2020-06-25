str=input('Enter string')
s1=str.split(',')
sub='';sum=0
for i in s1:
    sum=0
    s2=i.split(':')
    r=len(s2[0])
    p=s2[0]
    for i in s2[1]:
        sum+=(int(i)**2)
    if sum%2==0:
        sub=p[r-2:r]+p[0:r-2]
    else:
        sub=p[1:]+p[0]
    print(sub,end=' ')
        
