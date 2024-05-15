import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

min_mix = sys.maxsize
start, end = 0, N-1
min_start, min_end = 0, N-1

while start < end:
    mix = liquid[start] + liquid[end]

    if min_mix > abs(mix):
        min_mix = abs(mix)
        min_start, min_end = start, end
    if mix == 0:
        break

    elif mix < 0:
        start += 1
    elif mix > 0:
        end -= 1

print(liquid[min_start], liquid[min_end])