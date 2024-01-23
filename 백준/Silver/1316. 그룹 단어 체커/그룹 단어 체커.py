import sys
read = sys.stdin.readline

n = int(read())
ans = 0
for _ in range(n):
    s = read()
    for i in range(len(s)-1):
        if (s[i] != s[i+1]) and (s[i] in s[i+1:]):
            break
        if i == len(s) - 2: ans += 1
print(ans)