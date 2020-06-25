str=input('enter string')
h=len(str)
for i in range(h//2,0,-1):
    prefix=str[0:i]
    suffix=str[h-i:h]
    if suffix==prefix:
        print(len(prefix))
        break
    
