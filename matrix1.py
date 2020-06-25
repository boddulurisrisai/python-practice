n,m=map(int,input('Enter numbers').split())
l=[];arr=[]
for i in range(n):
    l.append(input().split())
for i in range(n):
    for j in range(m):
        if j<m-3:
            if l[i][j]==l[i][j+1]==l[i][j+2]==l[i][j+3]:
                arr.append(l[i][j])
        if i<n-3:
            if l[i][j]==l[i+1][j]==l[i+2][j]==l[i+3][j]:
                arr.append(l[i][j])
        if i>=3 and j<m-3:
            if l[i][j]==l[i-1][j+1]==l[i-2][j+2]==l[i-3][j+3]:
                arr.append(l[i][j])
        if i>=3 and j>=3:
            if l[i][j]==l[i-1][j-1]==l[i-2][j-2]==l[i-3][j-3]:
                arr.append(l[i][j])
print(min(arr))
        
