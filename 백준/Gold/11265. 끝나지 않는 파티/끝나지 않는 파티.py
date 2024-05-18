import sys, heapq
INF = float('inf')
input = sys.stdin.readline

def dijktra(start, end):
    visited = [INF] * N
    heap = list()
    visited[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        time, party = heapq.heappop(heap)
        if visited[party] < time:
            continue
        for next_party, plus_time in enumerate(graph[party]):
            next_time = time + plus_time
            if visited[next_party] > next_time:
                visited[next_party] = next_time
                heapq.heappush(heap, (next_time, next_party))

    record[start] = visited
    return visited[end]

N, M = map(int, input().split()) # 파티장 크기, 손님 수
graph = [list(map(int, input().split())) for i in range(N)] # i -> j 가는데 걸리는 시간
record = [[] for i in range(N)]
for m in range(M):
    A, B, C = map(int, input().split()) # A -> B 가는데 C 시간 후에 파티가 열린다

    if record[A-1]:
        if record[A-1][B-1] <= C:
            print("Enjoy other party")
        else:
            print("Stay here")
    else:
        if dijktra(A-1, B-1) <= C:
            print("Enjoy other party")
        else:
            print("Stay here")
