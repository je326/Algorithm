import sys
from collections import deque
read = sys.stdin.readline

N, M, V = map(int, read().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [False for _ in range(N+1)]

def dfs(V):
    visited_dfs[V] = True
    print(V, end=" ")

    for nx in graph[V]:
        if not visited_dfs[nx]:
            dfs(nx)

def bfs(V):
    visited = [False for _ in range(N+1)]

    visited[V] = True
    ans = [V]
    
    Q = deque([V])

    while Q:
        c = Q.popleft()
        for nx in graph[c]:
            if not visited[nx]:
                Q.append(nx)
                visited[nx] = True
                ans.append(nx)
    print(" ".join(map(str, ans)))

dfs(V)
print()
bfs(V)