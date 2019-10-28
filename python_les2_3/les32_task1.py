s = input()
a = input()
b = input()

cnt = 0 
while a in s:
    cnt += 1
    if cnt > 1000:
        cnt = 'Impossible'
        break
    s = s.replace(a,b)

print(cnt)
