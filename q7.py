my_dict={
        "a":50,
   "b":58,
   "c":56,
   "d":40,
   "e":100,
   "f":200
}
list=[] 
for i in range(3):
    max=0
    for j in my_dict:
        if max<my_dict[j]:
            max=my_dict[j]
            a =j
    list.append(a)
    # print(a)
    my_dict.pop(a)
print(list)