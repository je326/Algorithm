import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
min_length = float('inf')
s = nums[0]
while True:
    if s >= S:
        min_length = min(min_length, end - start + 1)
        s -= nums[start]
        start += 1
    else:
        end += 1
        if end == N: break
        s += nums[end]

if min_length != float('inf'):
    print(min_length)
else: print(0)