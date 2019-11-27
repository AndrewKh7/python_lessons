import json

def func(obj_):
    obj = dict() 
    for o in obj_:
        obj[o['name']] = o['parents']
    res = dict()
    parent_set = set()

    def traverse(child):
        #nonlocal res
        for p in obj[child]:
            if p not in parent_set:
                parent_set.add(p)
                if p in res:
                    res[p] += 1
                else:
                    res[p] = 1
                traverse(p)

    for key in obj:
        if key in res:
            res[key] += 1
        else:
            res[key] = 1

        parent_set.clear()
        traverse(key)
    return res


if __name__ == '__main__':
    with open('./file.json') as f:
        ouput = sorted(func(json.loads(input())).items(),key = lambda kv:(kv[0], kv[1]))
    for key,it in ouput:
        print(key,':',it)
 
