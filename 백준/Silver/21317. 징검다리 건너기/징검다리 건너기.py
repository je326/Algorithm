import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
stones = []
for i in range(N-1):
    s, l = map(int, input().split())
    stones.append((s, l))

K = int(input())

dp = [0] * N 
ans = []
if N == 1:
    print(0)
elif N == 2:
    print(stones[0][0])
elif N == 3:
    print(min(stones[0][1], stones[0][0] + stones[1][0]))
elif N > 3:
    dp[1] = stones[0][0]
    #작은 점프, 큰 점프만 고려한 경우
    for i in range(2, N):
        dp[i] = min(dp[i-1] + stones[i-1][0], dp[i-2] + stones[i-2][1])
    ans.append(dp[N-1])
    #매우 큰 점프 고려
    for j in range(N-3):
        dp2 = deepcopy(dp)
        dp2[j+3] = dp[j] + K
        for k in range(j+4, N):
            dp2[k] = min(dp2[k-1] + stones[k-1][0], dp2[k-2] + stones[k-2][1])
        ans.append(dp2[N-1])
    print(min(ans))
