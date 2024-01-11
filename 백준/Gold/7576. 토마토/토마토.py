from collections import deque
import sys
read = sys.stdin.readline

M, N = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]

Q = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            Q.append([i,j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while Q:
        x,y = Q.popleft() 
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                Q.append([nx, ny])
                
bfs()
ans = 0

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans - 1)
