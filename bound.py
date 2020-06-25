import re
str=input('enter the string')
ones=re.findall('[abdgopqADOPQR069]',str)
two=re.findall('[B8]',str)
print(len(ones)+(len(two)*2))
