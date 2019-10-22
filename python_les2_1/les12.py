a = 4
b = a
c = 4
objects = (a,b,c)
res = set()
for i in objects:
    res.add(id(i))
print(res)
print(len(res))
