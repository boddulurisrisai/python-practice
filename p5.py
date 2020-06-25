l=input().split(',')
for i in l:
    sum1=0
    s=''
    p,n=i.split(':')
    for j in n:
        sum1=int(j)**2
    if sum1%2==0:
        last=p[-1]
        s=last+p[0:len(p)-1]
    else:
        firs=p[-2:]
        s=firs+p[2:len(p)-2]
    print(s,end=' ')
    
