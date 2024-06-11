import sys
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

profit = 0
for i in range(N):
    profit = max(dp[i], profit)
    if i + schedule[i][0] > N:
        continue
    dp[i + schedule[i][0]] = max(profit + schedule[i][1], dp[i + schedule[i][0]])
    
print(max(dp))
