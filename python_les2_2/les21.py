#'''
#tsak 1
#,,,
n = int(input())
exceptions = [input() for i in range(n)]
dict_of_ex = dict()
for ex in exceptions:
    v = ex.split(':')
    if len(v) == 1 :
        dict_of_ex[v[0].strip()] = []
    else
        dict_of_ex[v[0].strip()] = v[-1].split()
m = int(input())
try_ex = [input() for i in range(m)]

set_of_checked_except = set()
output = list()

for i in try_ex:
    if i in set_of_checked_except:
        print(i)
        continue
    for j in dcir_of_ex[i]
        if j in set_of_checked_ex:
            print(j)
            break
    
