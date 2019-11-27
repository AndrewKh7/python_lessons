import re
import requests as rq


url1 = input()
url2 = input()

url1_res = rq.get(url1)
#print(url1_res.text)
#iurl2_res = rq.get(url2)
#print(ur2_res.text)
flag = 'No'
for link in  re.findall(r'(?<=href=")([\w:./]+)',url1_res.text):
    link_res = rq.get(link)
    if link_res.status_code == 200:
        for link2 in  re.findall(r'(?<=href=")[\w:./]+',link_res.text):
            if link2 == url2:
                flag = 'Yes'
                break
    
print(flag)

