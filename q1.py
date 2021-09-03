string="MISSISSIPPI"
t=list(string)
a=[]
i=0
n={}
while i<len(t):
    j=0
    count=0
    
    while j<len(t):
        if t[i]==t[j]:
            count=count+1
        j=j+1
    if t[i] in a:
        i+=1
        continue
    a.append(t[i])
    print(t[i],count)
    n.update({t[i]:count})
print(n)