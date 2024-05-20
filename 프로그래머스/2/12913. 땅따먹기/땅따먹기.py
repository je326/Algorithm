def solution(land):
    answer = 0
    
    N = len(land)
    dp = [[0] * 4 for i in range(N)]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, N):
        for j in range(4):  
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + land[i][j]) 
    answer = max(dp[N-1])
    return answer