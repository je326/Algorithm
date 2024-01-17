import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
graph = [list(map(int, read().split())) for _ in range(N)]


#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
    Q = deque([(x, y)])
    visited[x][y] = True
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > h:
                Q.append((nx, ny))
                visited[nx][ny] = True

#그래프 내에서 가장 높은 높이 찾기
height = 0
for i in range(N):
    for j in graph[i]:
        if height < j:
            height = j

#물에 잠기지 않은 지역 수 세기
ans = 0
for h in range(height + 1):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, h)
                count += 1
    ans = max(ans, count)

print(ans)