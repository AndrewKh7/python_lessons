#task 1
f = open('./text.txt')
str1 = ''
line = f.readline()
# for i in range(len(line)):
#     if not (i % 2):
#          str1+=line[i]*int(line[i+1])
print(line.split('[-+]?\d+')
# f.write(str1)
f.close()
