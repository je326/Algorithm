from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True
    temp = 1

    while queue:
        v = queue.popleft()

        for i in range(4):
            new_v = (v[0] + dx[i], v[1] + dy[i])
            if 0 <= new_v[0] < N and 0 <= new_v[1] < N and graph[new_v[0]][new_v[1]] == 1 and not visited[new_v[0]][new_v[1]]:
                visited[new_v[0]][new_v[1]] = True
                queue.append(new_v)
                temp += 1

    ans.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs((i, j))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
