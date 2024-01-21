import sys

read = sys.stdin.readline

N = int(read())
nums = [0] + [int(read()) for i in range(N)]
ans = []

#i=현재 좌표, j=시작한 좌표
def dfs(i, j):
    visited[i] = True
    w = nums[i]
    if not visited[w]:
        dfs(w, j)
    elif visited[w] and w == j:
        ans.append(w)

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)