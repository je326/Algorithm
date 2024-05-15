T = int(input())
for tc in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0 for i in range(N)] for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    if N >= 2:
        for i in range(1, N):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + stickers[0][i])
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] + stickers[1][i])

    print(max(dp[0][N-1], dp[1][N-1]))
