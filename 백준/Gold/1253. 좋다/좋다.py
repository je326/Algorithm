import sys
input = sys.stdin.readline

def search(arr, idx):
    start, end = 0, len(arr)-1
    while start < end:
        if arr[start] + arr[end] > nums[idx]:
            end -= 1
        elif arr[start] + arr[end] < nums[idx]:
            start += 1
        elif arr[start] + arr[end] == nums[idx]:
            return 1
    return 0

ans = 0
N = int(input())
nums = list(map(int, input().split()))

nums.sort()
for i in range(len(nums)):
    ans += search(nums[:i] + nums[i+1:], i)

print(ans)