
import sys
import re


for line in sys.stdin:
    if line == '@@@': break
    if re.findall(r'(\b(\w+)\2){1}\b',line):
        print(line.strip('\n'))

