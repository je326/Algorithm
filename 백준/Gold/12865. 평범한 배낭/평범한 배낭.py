import sys
input = sys.stdin.readline

N, K = map(int, input().split())

objects = []
for _ in range(N):
    W, V = map(int, input().split())
    objects.append((W, V))

dp = [[0] * (K+1) for i in range(N+1)]
for i in range(1, N+1):
    w, v = objects[i-1]
    for j in range(1, K+1):

        if w <= j:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
        else: 
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
