#task 1 
# a = [int(i) for i in input().split()]
# s = 0
# for i in a:
#     s += i
# print(s)

# task 2
# val = [int(i) for i in input().split()]
# if len(val) == 1: 
#     print(val[0])
# elif len(val) == 2:
#     print(val[1]*2,2*val[0])
# else:
#     res = [0]* len(val)
#     res[0] = val[1]+val[-1]
#     for i in range(1,len(val)-1):
#          res[i] = val[i-1]+val[i+1]
#     res[-1] = val[-2]+val[0]
#     [print(i, end = ' ') for i in res]
    
# task 3
val = [int(i) for i in input().split()]
val.sort()
res =[]
last = ''
for i in val:
    if i == last and not res.count(i): res.append(i)
    last = i
[print(i, end = ' ') for i in res]


