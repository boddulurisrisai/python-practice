m,n=map(int,input().split())
l=[];q=[]
for i in range(m):
    l.append(input().split())
for i in range(m):
    for j in range(n):
        if j<n-3:
            if l[i][j]==l[i][j+1]==l[i][j+2]:
                q.append(l[i][j])
        if i<m-3:
            if l[i][j]==l[i+1][j]==l[i+2][j]:
                q.append(l[i][j])
        if i>=2 and j<n-2:
            if l[i][j]==l[i-1][j+1]==l[i-2][j+2]:
                q.append(l[i][j])
        if i>=2 and j>=2:
            if l[i][j]==l[i-1][j-1]==l[i-2][j-2]:
                q.append(l[i][j])
if len(q)==0:
    print(-1)
else:
    print(min(q))
