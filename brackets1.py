def find(s):
    stack=[]
    count=0
    for i in s:
        if i=='(' or i=='[' or i=='{':
            stack.append(i)
            count+=1
            continue
        if len(stack)==0:
            return count+1
        x=stack.pop()
        if i==')' and x=='(':
            count+=1
        elif i==']' and x=='[':
            count+=1
        elif i=='}' and x=='{':
            count+=1
        else:
            return count+1
    if len(stack)==0:
        return 0
    else:
        return count+1
s=input('enter string')
q=find(s)
print(q)
