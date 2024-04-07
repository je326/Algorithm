import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

map = [list(map(int, input().split())) for i in range(R)]

#공기청정기 위치 찾기
for i in range(R):
    if map[i][0] == -1:
        cleaner = (i, i+1)
        break

#미세먼지 확산
def spread():
    temp_map = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if map[i][j] > 0:
                spread_amount = map[i][j]//5
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C and map[nx][ny] != -1:
                        temp_map[nx][ny] += spread_amount
                        temp_map[i][j] -= spread_amount

    #원본 map 업데이트
    for i in range(R):
        for j in range(C):
            if map[i][j] != -1:
                map[i][j] += temp_map[i][j]

# 공기청정기 작동
def clean():
    upper, lower = cleaner

    # 위쪽 순환
    for i in range(upper - 1, 0, -1):
        map[i][0] = map[i - 1][0]
    for i in range(C - 1):
        map[0][i] = map[0][i + 1]
    for i in range(upper):
        map[i][C - 1] = map[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        map[upper][i] = map[upper][i - 1]
    map[upper][1] = 0

    # 아래쪽 순환
    for i in range(lower+1, R-1):
        map[i][0] = map[i+1][0]
    for i in range(C-1):
        map[R-1][i] = map[R-1][i+1]
    for i in range(R-1, lower, -1):
        map[i][C-1] = map[i-1][C-1]
    for i in range(C-1, 1, -1):
        map[lower][i] = map[lower][i-1]
    map[lower][1] = 0

for _ in range(T):
    spread()
    clean()

# 미세먼지 양 계산
ans = sum(sum(row) for row in map) + 2
print(ans)