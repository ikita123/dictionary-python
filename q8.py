a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dic={}
for i in a:
     s=a[i]
     for i in a:
         f=a[i]
         if f<s:
            dic[i]=f
for i in a:
    s=a[i]
    for i in a:
        f=a[i]
        if f>s:
            dic[i]=f
print(dic)
