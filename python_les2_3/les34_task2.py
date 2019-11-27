import requests as rq
import re


url = input()
html = rq.get(url)
links = re.findall(r'<a.*?href ?= ?[\'|\"](.{1,5}:\/\/)?([\w_-]+(\.[\w_-]+){1,3})([\/|:].*)?[\'|\"].*>',html.text)
res = set()
for link in links:
    res.add(link[1])
res = list(res)
res.sort()
for i in res:
    print(i)
