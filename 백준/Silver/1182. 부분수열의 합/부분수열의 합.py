import sys
input = sys.stdin.readline

def dfs(start, temp):
    global cnt
    if start > 0 and temp == S:
        cnt += 1
    for i in range(start, len(nums)):
        temp += nums[i]
        dfs(i+1, temp)
        temp -= nums[i]

N, S = map(int, input().split())
nums = list(map(int, input().split()))
temp = 0
cnt = 0

dfs(0, temp)
print(cnt)
