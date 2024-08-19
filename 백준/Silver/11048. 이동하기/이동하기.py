import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rooms = [0 for i in range(N)] 
for i in range(N):
    rooms[i] = list(map(int, input().split()))

dp = [[0] * M for i in range(N)]
dp[0][0] = rooms[0][0]

for i in range(N):
    for j in range(M):
        if i == 0 and j > 0:
            dp[i][j] = rooms[i][j]+dp[i][j-1]
        elif i > 0 and j == 0:
            dp[i][j] = rooms[i][j]+dp[i-1][j]
        elif i > 0 and j > 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + rooms[i][j]

print(dp[N-1][M-1])
