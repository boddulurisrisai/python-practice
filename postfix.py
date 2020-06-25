t=int(input())
stack=[]
while(t!=0):
    s=input('enter expression')
    for i in s:
        if i.isdigit():
            stack.append(i)
        else:
            b=stack.pop()
            a=stack.pop()
            if i=='*':
                c=int(a)*int(b)
                stack.append(c)
            elif i=='-':
                c=int(a)-int(b)
                stack.append(c)
            elif i=='+':
                c=int(a)+int(b)
                stack.append(c)
            elif i=='%':
                c=int(a)%int(b)
                stack.append(c)
            else:
                c=int(a)//int(b)
                stack.append(c)
                
    print(stack.pop())           
    t-=1
            
