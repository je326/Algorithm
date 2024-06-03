import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lamps = [list(input().rstrip()) for i in range(N)]
K = int(input())

ans = 0
for lamp in lamps:
    off = lamp.count("0")
    temp = 0
    if off <= K and off % 2 == K % 2:
        for lamp2 in lamps:
            if lamp == lamp2:
                temp += 1
        ans = max(temp, ans)

print(ans)
