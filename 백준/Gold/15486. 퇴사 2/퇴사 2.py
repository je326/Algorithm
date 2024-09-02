import sys
input = sys.stdin.readline

N = int(input())
schedule = [0] * (N+1)
for i in range(N):
    T, P = map(int, input().split())
    schedule[i+1] = (T, P)

dp = [0] * (N+2)

for i in range(1, N+1):
    T, P = schedule[i]

    dp[i] = max(dp[i], dp[i-1])

    if (i + T - 1 <= N):
        dp[i+T] = max(dp[i+T], P + dp[i])
    
print(max(dp))