import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

def bfs(v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = True
    sheep = 0
    wolf = 0

    while queue:
        v = queue.popleft()

        if graph[v[0]][v[1]] == 'o':
            sheep += 1
        elif graph[v[0]][v[1]] == 'v':
            wolf += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_v = (v[0] + dx, v[1] + dy)
            if 0 <= next_v[0] < R and 0 <= next_v[1] < C and not visited[next_v[0]][next_v[1]] and graph[next_v[0]][next_v[1]] != '#':
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)

    if sheep > wolf:
         wolf = 0
    else:
         sheep = 0

    return sheep, wolf

total_sheep = 0
total_wolf = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and not visited[i][j]:
            sheep, wolf = bfs((i, j))
            total_sheep += sheep
            total_wolf += wolf

print(total_sheep, total_wolf)

