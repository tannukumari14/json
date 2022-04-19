# import json
# a=["tanu","18","2004","12"]
# b={}
# keys=["name","age","year","class"]
# c=({'b':b})
# for i in range (len(a)):
#     b.update({keys[i]:a[i]})
# with open("tanu q no1",'w')as g:
#     json.dump(c,g,indent=7)

import json
a=["name","class","age","year"]
b={}
c=["sheetal","12","19","2002"]
d=[{"b":b}]
for i in range(len(a)):
    b.update({a[i]:c[i]})
with open("sneha q1","w")as g:
    json.dump(d,g,indent=3)