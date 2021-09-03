name=["nikita","chaya","karuna","saloni","priyanka","yogita","gouri","priti","naina","neha"]
marks=[100,90,80,79,60,50,40,30,20,10]
a={}
i=0
j=0
while i<len(name):
    a.update({name[i]:marks[j]})
    j+=1
    i+=1
print(str(a))