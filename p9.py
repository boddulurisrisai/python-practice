s=list(input())
c1=[]
for i in range(len(s)):
    if s[i]=='':
        continue
    c2=s[i]
    for j in range(i+1,len(s)):
        if s[i].lower()==s[j].lower():
            c2+=s[j]
            s[j]=''
    s[i]=''
    c1.append(c2)
for i in range(len(c1)):
    for j in range(i+1,len(c1)):
        if c1[i].lower()>c1[j].lower():
            temp=c1[i]
            c1[i]=c1[j]
            c1[j]=temp

s3=''
for i in range(len(c1)//2):
    print(c1[i],c1[len(c1)-i-1],end=' ')
if(len(c1)%2!=0):
    print(c1[len(c1)//2])
        
