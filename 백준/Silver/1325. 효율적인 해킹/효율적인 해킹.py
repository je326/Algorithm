import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    cnt = 1
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()

        for c in computers[v]:
            if not visited[c]:
                queue.append(c)
                visited[c] = True
                cnt += 1
    
    return cnt

N, M  = map(int, input().split())

computers = [[] for i in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    computers[B].append(A)

cnt_arr = [0] * (N+1)
max_cnt = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    cnt = bfs(i)
    cnt_arr[i] = cnt
    max_cnt = max(max_cnt, cnt)

ans = []
for i in range(1, N+1):
    if cnt_arr[i] == max_cnt:
        print(i, end=" ")
