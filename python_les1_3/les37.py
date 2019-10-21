# # task1
# n = int(input())
# games = []
# for i in range(n):
#     game = input().split(';')
#     games.append(game)

# team = {}
# for i in games:
#     if i[0] in team:
#         team[i[0]][0] += 1
#     else:
#         team[i[0]] = [1,0,0,0,0]
#     if i[2] in team:
#         team[i[2]][0] += 1
#     else:   
#         team[i[2]] = [1,0,0,0,0]
#     if i[1] < i[3]:
#         team[i[2]][1] += 1
#         team[i[2]][4] += 3
#         team[i[0]][3] += 1
#     elif i[1] == i[3]:
#         team[i[2]][2] += 1
#         team[i[0]][2] += 1
#         team[i[2]][4] += 1
#         team[i[0]][4] += 1
#     else:
#         team[i[0]][1] += 1
#         team[i[0]][4] += 3
#         team[i[2]][3] += 1

# for i in team:
#     print(i,end = ':')
#     [print(j,end = ' ') for j in team[i]]
#     print()

# # task2
# alp = input()
# key = input()
# str1 = input()
# str2 = input()
# str_out1 = ''
# str_out2 = ''
# for i in str1:
#     str_out1 += key[alp.index(i)]
# for i in str2:
#     str_out2 += alp[key.index(i)]
# print(str_out1) 
# print(str_out2) 

# task3
# d = int(input())
# words = {input().lower() for i in range(d)}
# l = int(input())
# sen = {input().lower() for i in range(l)}
# for i in sen:
#     for j  in i.split():
#         if j not in words:
#             print(j)
#             words.add(j)
            

# task4
# n = int(input())
# commands = [input().lower() for i in range(n)]

# endd = [0,0]
# for k in commands:
#     i,j = k.split(' ')
#     if i == 'север':
#         endd[1]+=int(j)
#     elif i == 'юг':
#         endd[1]-=int(j)
#     elif i == 'запад':
#         endd[0]-=int(j)
#     elif i == 'восток':
#         endd[0]+=int(j)
# print(endd[0],endd[1])

# task5
f = open('table.txt',encoding='utf-8')
c = [[] for i in range(11)] 
for i in f:
    arr = i.strip('\n').split()
    arr[0] = int(arr[0])
    arr[2] = int(arr[2])
    c[arr[0]-1].append(arr[2])


for i in range(11):
    if c[i] != []:
        print(i+1, sum(c[i])/len(c[i]))
    else:
        print(i+1, '-')
