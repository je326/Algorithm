from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] += 1

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dx[i], v[1] + dy[i])
            if 0 <= next_v[0] < N and 0 <= next_v[1] < M and graph[next_v[0]][next_v[1]] == 1 and visited[next_v[0]][next_v[1]] == 0:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                queue.append(next_v)
    return visited[N-1][M-1]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

print(bfs((0,0)))