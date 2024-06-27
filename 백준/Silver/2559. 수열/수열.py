import sys

input = sys.stdin.readline
N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

start, end = 0, K-1
temp = sum(temperatures[start:end+1])
ans = temp

start += 1
end += 1

while end < N:
    temp -= temperatures[start-1]
    temp += temperatures[end]

    start += 1
    end += 1

    ans = max(ans, temp)

print(ans)