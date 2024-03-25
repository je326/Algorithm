from collections import deque
import sys

input = sys.stdin.readline

def dfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()

        if v == K:
            global cnt
            cnt += 1
            continue

        for new_v in [v+1, v-1, v*2]:
            if 0 <= new_v <= MAX and (arr[new_v] == 0 or arr[new_v] == arr[v] + 1):
                arr[new_v] = arr[v] + 1
                queue.append(new_v)


MAX = 100_000
N, K = map(int, input().split())
arr = [0 for _ in range(MAX+1)]
cnt = 0

dfs(N)
print(arr[K])
print(cnt)