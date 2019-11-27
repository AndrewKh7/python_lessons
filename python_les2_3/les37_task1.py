from  xml.etree import ElementTree as et


tree = et.fromstring(input())

res = {'red':0,'green':0,'blue':0}

def func(elem,level=1):
    res[elem.attrib['color']] += level
    for child in elem:
        func(child, level = level + 1)

func(tree)

for color in res:
    print(res[color], end=' ')

