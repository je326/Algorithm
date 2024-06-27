import sys

input = sys.stdin.readline
N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

temp = sum(temperatures[:K])
ans = temp

for idx in range(1, N-K+1):
    temp = temp - temperatures[idx-1] + temperatures[idx+K-1]
    ans = max(ans, temp)

print(ans)
