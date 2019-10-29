import sys
import re


for line in sys.stdin:
    if line == '@@@': break
   # if re.search(r".*cat.*cat.*",line, re.IGNORECASE):
    if len(re.findall(r'cat',line,re.IGNORECASE))>1:
        print(line.strip('\n'))
