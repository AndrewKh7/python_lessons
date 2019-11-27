import csv

res = dict()

with open('./Crimes.csv') as f:
    reader = csv.reader(f)
    first_row = next(reader)
    Date = first_row.index('Date')
    PT = first_row.index('Primary Type')
    for row in reader:
        if row[Date][8:10] == '15':
            if row[PT] in res:
                res[row[PT]] += 1
            else:
                res[row[PT]] = 1
for k,i in sorted(res.items(),key = lambda kv:kv[1]):
    print(k+': '+str(i))

print('Most often: ')
print( sorted(res.items(),key = lambda kv:kv[1])[-1]) 
