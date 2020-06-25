import re
str=input('enter string')
s1=re.findall('[a-zA-Z]',str)
s1=s1[::-1]
for i in range(len(str)):
    if str[i]=='#' or str[i]=='@':
        s1.insert(i,str[i])
print(s1)
