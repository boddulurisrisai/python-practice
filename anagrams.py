from itertools import permutations
t=int(input())
b=[]
while(t!=0):
    s1=input('enter string')
    s2=input('enter another string')
    s11=[0]*26
    s22=[0]*26
    for i in range(len(s1)):
        s11[ord(s1[i])-97]+=1
    for j in range(len(s2)):
        s22[ord(s2[j])-97]+=1
    dele=0
    for i in range(26):
        dele+=abs(s11[i]-s22[i])
    print(dele)
    t-=1
    
