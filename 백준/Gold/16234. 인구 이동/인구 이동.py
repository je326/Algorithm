from collections import deque
import sys

input = sys.stdin.readline

queue = deque([])
def bfs(v):
    queue.append(v)
    opened_countries = [(v[0], v[1])]

    while queue:
        v = queue.popleft()

        for i in range(4):
            new_v = (v[0]+dx[i], v[1]+dy[i])
            if ((0 <= new_v[0] < N) and (0 <= new_v[1] < N) and (L <= abs(graph[v[0]][v[1]] - graph[new_v[0]][new_v[1]]) <= R)
                    and not visited[new_v[0]][new_v[1]]):
                queue.append(new_v)
                opened_countries.append((new_v[0], new_v[1]))
                visited[new_v[0]][new_v[1]] = True

    if len(opened_countries) > 1:
        result = sum(graph[c[0]][c[1]] for c in opened_countries) // len(opened_countries)
        for c in opened_countries:
            graph[c[0]][c[1]] = result

        return 1
    else:
        return 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    move = False
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                move |= bfs((i, j))
    if move:
        ans += 1
    else:
        break

print(ans)