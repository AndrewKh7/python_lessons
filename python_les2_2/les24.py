l = list()
with open('./file.txt') as f:
    for lin in f.readlines():
        l.append(lin)
with open('./out.txt','w') as o:
    for i in l[-1::-1]:
        o.write(i)
