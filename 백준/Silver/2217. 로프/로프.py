import sys
read = sys.stdin.readline

N = int(read())
roap = []

for i in range(N):
    roap.append(int(read()))
roap.sort()

ans = []
for i in roap:
    ans.append(i*N)
    N-=1

print(max(ans))