import os
output_path = []
for p,d,f in os.walk('./main'):
    for i in f:
        if i[-3:] == '.py':
            output_path.append(p[2:])
            break

output_path.sort()
for i in output_path:
        print(i)
with open('../out.txt','w') as file_:
    file_.write('\n'.join(output_path))
