def find(str1):
     for i in range(len(str1)):
         if str1[i]=='#':
             if a=='Z':
                 str1[i]='A'
             else:
                 str1[i]=chr(ord(a)+1)
         else:
             a=str1[i]
    
     return ''.join(str1)

str1=list(input('enter string 1'))
str2=list(input('enter string 2'))
s=find(str1)
s2=find(str2)
if s==s2:
    print('Yes')
else:
    print('No')
