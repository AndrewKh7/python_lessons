#import datetime
#y,m,d = tuple(int(i) for i in input().split())
#mydate = datetime.date(y,m,d)
#days = datetime.timedelta(int(input()))
#mydate+=days
#t = mydate.timetuple()
#for i in range(3): 
#    print(t[i], end = ' ')
#

#task2
print('Start1')
from simplecrypt import encrypt, decrypt
print('Start2')
encr = open('./encrypted.bin','rb').read()
print(str(encr))
pasw =  open('./passwords.txt','r') 
for p in pasw.readlines():
    print('Checking: ' + p.replace('\n',''))
    try:
        print( decrypt(p.replace('\n',''),encr ))
    except Exception as e:
       print(' Wrong! '+str(e))
    
