import sys
input = sys.stdin.readline

def dfs(start, ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(start, len(nums)):
        ans.append(nums[i])
        dfs(i, ans)
        ans.pop()


N, M = map(int, input().split())
nums = sorted(set(list(map(int, input().split()))))

ans = []
dfs(0, ans)
