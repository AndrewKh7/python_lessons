import sys
import re

for line in sys.stdin:
    if re.fullmatch(r'[0|1]+',line).group()[0]:
        temp = re.fullmatch(r'0*(11)*0*',line[::-1]).group()[0]
        if temp:
            print(temp)
        else:
            print('NO: ', temp)
    else:
        print('not a number')
