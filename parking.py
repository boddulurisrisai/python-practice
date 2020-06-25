def find(a):
    free=a[0]
    laneno=0
    for i in range(2,5):
        if free<a[i]:
            a[i]=free
            laneno=i
    return laneno
            
        
l=['T','A','B','C','D']
p=[];a=[]
for i in range(1,5):
    b=input().split(',')
    if b[0]!='-1':
        booked=len(b)
        a[i]=10-booked
w=int(input())
if(sum(a)<w):
    print('X')
else:
    while(w!=0):
        laneno=find(a)
        booked=10-a[laneno]
        while(w!=0 and booked!=10):
            booked+=1
            p.append(l[laneno]+str(booked))
            w-=1
        a[laneno]=10-booked
print(p)
        
    
    
