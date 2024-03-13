from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()

        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)
