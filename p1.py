l=list(input().split(','))
p=l.index('5')
q=l.index('8')
r=l[p:q+1]
t=l[0:p]
t.extend(l[q+1:])
z=sum(list(map(int,t)))
x=''.join(r)
print(z+int(x))