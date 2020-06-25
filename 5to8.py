'''l=list(input('Enter list values').split(','))
sum=0;c=0;d=0
s1=''
for i in range(len(l)):
    if l[i]=='5':
        c=i
    if l[i]=='8':
        d=i
for i in range(len(l)):
    if i>=c and i<=d:
        s1+=l[i]
    else:
        sum+=int(l[i])
num=s1
q=int(num)+sum
print(q)'''


l=input('enter values').split(',')
left=l.index('5')
right=l.index('8')
sum=0;s1=''
for i in range(left,right+1):
    s1+=''.join(l[i])
for i in range(len(l)):
    if i<left or i>right:
        sum+=int(l[i])
print(sum+int(s1))
        
