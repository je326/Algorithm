import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(computers, visited, heap, start):
    visited[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        w, v = heapq.heappop(heap)
        if visited[v] < w:
            continue
        for next_v, added_w in computers[v]:
            next_w = w + added_w
            if next_w < visited[next_v]:
                visited[next_v] = next_w
                heapq.heappush(heap, (next_w, next_v))


T = int(input())

for tc in range(T):
    N, D, C = map(int, input().split())
    computers = [[] for _ in range(N + 1)]
    visited = [INF] * (N + 1)
    heap = list()

    for d in range(D):
        a, b, s = map(int, input().split())
        computers[b].append((a, s))

    dijkstra(computers, visited, heap, C)

    cnt, ans = 0, 0
    for i in visited:
        if i != INF:
            cnt += 1
            ans = max(ans, i)

    print(cnt, ans)
