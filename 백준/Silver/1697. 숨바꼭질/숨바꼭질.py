from collections import deque
import sys

input = sys.stdin.readline

def dfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        if v == M:
            return ans[v]
        else:
            for new_v in [v+1, v-1, 2*v]:
                if 0 <= new_v <= MAX and ans[new_v] == 0:
                    ans[new_v] = ans[v] + 1
                    queue.append(new_v)

MAX = 100_000
ans = [0 for _ in range(MAX+1)]
N, M = map(int, input().split())

print(dfs(N))