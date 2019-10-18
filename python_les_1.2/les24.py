# task1
# Gemeni = input()
# Gemeni = Gemeni.lower()
# cnt = Gemeni.count('g')+Gemeni.count('c')
# print(cnt/len(Gemeni)*100)

# #####
# s = 'abcdefghijk'
# print(s[3:6],end=' ')
# print(s[:6],end=' ')
# print(s[3:],end=' ')
# print(s[::-1],end=' ')
# print(s[-3:],end=' ')
# print(s[:-6],end=' ')
# print(s[-1:-10:-2],end=' ')

# task 2
str1 = input()
i = 1
res = ''
cnt = 1
length = len(str1)
while i < length:
    if str1[i] == str1[i-1]:
        cnt += 1
    else:
        res += str1[i-1]+str(cnt)
        cnt = 1
    i+=1
res+=str1[i-1]+str(cnt)
print(res)

