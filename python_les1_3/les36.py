#task1
# import requests
# r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/168.txt')
# t = r.text
# t = t.strip()
# t = t.split('\n')
# # f = open('req_text.txt','x')
# # f.write(str(r.text))
# print(t)
# # for i in t:
# #     print(i)
# print(len(t))


#task2
import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt' 
r = requests.get(url)
while r.text.split()[0] != 'We':
    url = '/'.join(url.rsplit('/')[:-1])+'/'+r.text
    r = requests.get(url)
    print(r.text)
print(r.text())
    