a=input('Enter a number')
l=[]
for i in range(len(a)):
    if i%2!=0:
        l.append(str(pow(int(a[i]),2)))

s=''.join(l)
print(s[0:4])
