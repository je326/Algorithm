import sys
input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0
for h in range(1, W-1):
    left_max = max(heights[:h+1])
    right_max = max(heights[h:])

    if heights[h] < min(left_max, right_max):
        ans += min(left_max, right_max) - heights[h]
        
print(ans)