import json
list1=["neelam","progrmer","24","2400",]
list2=["komal","trainer","24","20000"]
list3=["anuradha","hr","25","40000"]
list4=["abhishek","manger","29","63000"]
b={}
c={}
d={}
e={}
keys=["name","Designation","Age",'Salary']
c=({'b':b,'c':c,"d":d,"e":e})
for j in range (len(list1)):
    b.update({keys[j]:list1[j]})
for k in range (len(list1)):
    c.update({keys[k]:list1[k]})
for i in range (len(list1)):
    d.update({keys[i]:list1[i]})
for m in range (len(list1)):
    b.update({keys[m]:list1[m]})
with open("meraki q no1",'w')as g:
    json.dump(c,g,indent=7)