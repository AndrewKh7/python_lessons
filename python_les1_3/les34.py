# #task 1
# f = open('./text.txt')
# str1 = ''
# line = f.readline()
# # for i in range(len(line)):
# #     if not (i % 2):
# #          str1+=line[i]*int(line[i+1])
# print(line.split('[-+]?\d+')
# # f.write(str1)
# f.close()

# task2
# import re
# def readfile(filename):
#     f =  open('./'+filename,'r',encoding='utf-8').read().lower()
#     return re.split(r'\W+',f) 
# d = {}
# for i in readfile('dataset_3363_3.txt') :
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# m = 0
# key = []
# for k,v in d.items():
#     if m < v:
#         m = v
#         key.clear()
#         key.append(k)
#     elif m == v:
#         key.append(k)
# print(min(key),m)

# task3
d = {}

for i in open('./file.txt','r', encoding='utf-8'):
    l = i.split(';')
    d[l[0]] = [int(l[1]),int(l[2]),int(l[3])]

mathematics = 0
physics = 0
rus_language = 0
for i in d:
    print(sum(d[i])/3)
    mathematics += d[i][0]
    physics += d[i][1]
    rus_language += d[i][2]
mathematics /= len(d)
physics /= len(d)
rus_language /= len(d)
print(mathematics, physics,rus_language)
