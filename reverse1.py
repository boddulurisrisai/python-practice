s=input('enter a string')
l=list(s)
s1=[];count=0;s2=[]
for i in l:
    count+=1
    if not i.isalpha():
        s1.append(i)
        s2.append(count-1)
s3=list(s[: :-1])
for i in range(len(s3)-1):
    if s3[i]=='#' or s3[i]=='@':
        s3.remove(s3[i])
for i in range(len(s3)):
    for j in range(len(s2)):
        if i==s2[j]:
            s3.insert(i,s1[j])
print(s3)
