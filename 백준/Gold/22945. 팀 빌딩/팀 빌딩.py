import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_status = 0
start, end = 0, N-1
while start < end:
    status = (end - start - 1) * min(arr[start], arr[end])
    max_status = max(max_status, status)
    if arr[start] <= arr[end]:
        start += 1
    else:
        end -= 1


print(max_status)
