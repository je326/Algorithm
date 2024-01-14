import sys
read = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(read())
graph = [list(read()) for _ in range(N)]

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
            dfs(nx,ny)


# 적록색약이 아닌 경우
visited = [[False] * N for _ in range(N)]
ans1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            ans1 += 1

# 적록색약인 경우
visited = [[False] * N for _ in range(N)]
ans2 = 0

#G와 R 같은 색상으로 인식
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j)
            ans2 += 1

print(ans1, ans2)