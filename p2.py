import re
s=input()
q=re.findall('[1-9]',s)
w=re.findall('[02468]',s)
q=list(set(q))
w=list(set(w))
q.sort(reverse=True)
w.sort(reverse=True)
if len(w)==0:
    print(-1)
else:
    if(int(q[-1])%2==0):
        print(''.join(q))
    else:
        q.remove(w[-1])
        q.append(w[-1])
        print(''.join(q))
