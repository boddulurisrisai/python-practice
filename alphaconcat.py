
str=list(input('Enter the string'))
g=[]
for i in range(len(str)):
    if str[i]=='':
        continue
    g1=str[i]
    for j in range(i+1,len(str)):
        if str[j].lower()==str[i].lower():
            g1+=str[j]
            print(g)
            str[j]=''
    str[i]=''
    g.append(g1)
for i in range(len(g)):
    for j in range(i+1,len(g)):
        if g[i].lower()>g[j].lower():
            temp=g[j]
            g[j]=g[i]
            g[i]=temp
length=len(g)
for i in range(length//2):
    print(g[i]+g[length-i-1],end='')
if length%2!=0:
    print(g[length//2])
