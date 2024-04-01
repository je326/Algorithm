import sys

input = sys.stdin.readline

N = int(input())
juice = [int(input()) for _ in range(N)]
dp = [0] * N

if N > 0:
    dp[0] = juice[0]
if N > 1:
    dp[1] = dp[0] + juice[1]
if N > 2:
    dp[2] = max(dp[1], dp[0] + juice[2], juice[1] + juice[2])

#현재 위치에서 최대로 마실 수 있는 경우
#1. dp[i-1]
#2. dp[i-2] + juice[i]
#3. dp[i-3] + juice[i-1] + juice[i]
    for i in range(3, N):
        dp[i] = max(dp[i-1], dp[i-2] + juice[i], dp[i-3] + juice[i-1] + juice[i])

print(dp[N-1])