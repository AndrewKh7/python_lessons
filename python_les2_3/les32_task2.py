s,t = (input() for _ in range(2))
cnt = 0
while len(s) >= len(t):
    i = s.find(t)
    if i == -1:
        break
    cnt += 1
    s = s[i+1:]
print(cnt)
