import sys
from itertools import combinations
input = sys.stdin.readline


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []

#집, 치킨집 좌표 따로 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        if city[i][j] == 2:
            chicken.append((i, j))

ans = 99999
#M개의 모든 조합에 대해 계산된 치킨 거리 중 최소값을 ans에 저장
for c in combinations(chicken, M):
    temp = 0
    for h in house:
       distance = 99999
       for i in range(M):
           distance = min(distance, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
       temp += distance
    ans = min(temp, ans)

print(ans)