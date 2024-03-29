import sys
read = sys.stdin.readline

N, M = map(int, read().split())

ans = []
def dfs(s):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(s, N+1):
        ans.append(i)
        dfs(i)
        ans.pop()

dfs(1)