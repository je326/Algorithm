import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
#0은 직사각형 외부, 1은 직사각형 내부
graph = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for i in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(ly, ry):
        for y in range(lx, rx):
            graph[x][y] = 1

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True
    temp = 1

    while queue:
        v = queue.popleft()

        for dx, dy  in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_v = (v[0] + dx, v[1] + dy)
            if 0 <= new_v[0] < M and 0 <= new_v[1] < N and graph[new_v[0]][new_v[1]] == 0 and not visited[new_v[0]][new_v[1]]:
                queue.append(new_v)
                visited[new_v[0]][new_v[1]] = True
                temp += 1

    return temp

cnt = 0
ans = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            temp = bfs((i, j))
            cnt += 1
            ans.append(temp)

ans.sort()
print(cnt)
print(*ans)
