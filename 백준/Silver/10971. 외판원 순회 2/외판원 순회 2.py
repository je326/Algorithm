import sys
input = sys.stdin.readline

def tsp(start, now, visited, sum_value):
    global ans
    if all(visited):
        if cities[now][start]:
            ans = min(ans, cities[now][start] + sum_value)
        return

    if sum_value > ans:
        return

    for i in range(N):
        if not visited[i] and cities[now][i]:
            visited[i] = True
            tsp(start, i, visited, sum_value + cities[now][i])
            visited[i] = False


N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
ans = float('inf')

for i in range(N):
    visited[i] = True
    tsp(i, i, visited, 0)
    visited[i] = False

print(ans)