l=list(map(int,input('enter list values:').split(',')))
p=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        first=l[i]
        second=l[j]
        s=[]
        s.append(first)
        s.append(second)
        for k in range(j+1,len(l)):
            if first+second==l[k]:
                s.append(l[k])
                first=second
                second=l[k]
        if len(p)<len(s):
            p=s
if len(p)>2:
    print(p)
else:
    print('-1')
        
            
                
            
        
