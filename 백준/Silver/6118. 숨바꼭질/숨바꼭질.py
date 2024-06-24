import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] += 1

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if visited[next_v] == 0:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

bfs(1)

max_distance = max(visited)
barn_num = visited.index(max_distance)
barns_cnt = visited.count(max_distance)

print(barn_num, max_distance-1, barns_cnt)