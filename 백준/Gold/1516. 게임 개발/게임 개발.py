from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

#진입 차수
indegree = [0] * (N+1)

#건물 정보(노드-간선)
building = [[] for i in range(N+1)]

#걸리는 시간
time = [0] * (N+1)

for i in range(1, N+1):
    temp = list(map(int, input().split()))[:-1]

    time[i] = temp[0]

    for t in temp[1:]:
        building[t].append(i)
        indegree[i] += 1

dp = [0] * (N+1)
queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    now = queue.popleft()

    for b in building[now]:
        indegree[b] -= 1
        dp[b] = max(dp[b], dp[now] + time[b])

        if indegree[b] == 0:
            queue.append(b)

for i in dp[1:]:
    print(i)

