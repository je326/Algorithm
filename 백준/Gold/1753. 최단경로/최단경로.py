import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    heap = []
    visited[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        w, v = heapq.heappop(heap)
        if visited[v] < w: continue

        for next_v, added_w in graph[v]:
            next_w = w + added_w
            if next_w < visited[next_v]:
                visited[next_v] = next_w
                heapq.heappush(heap, (next_w, next_v))


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
visited = [INF] * (V+1)

for e in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra()

for i in visited[1:]:
    if i == INF:
        print("INF")
    else: print(i)