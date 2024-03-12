from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()

        for i in range(4):
            new_v = (v[0] + dx[i], v[1] + dy[i])
            if 0 <= new_v[0] < N and 0 <= new_v[1] < M and graph[new_v[0]][new_v[1]] == 1 and not visited[new_v[0]][new_v[1]]:
                visited[new_v[0]][new_v[1]] = True
                queue.append(new_v)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())

    ans = 0
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs((i, j))
                ans += 1

    print(ans)
    