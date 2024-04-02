import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))

#중복을 방지하기 위해 2차원
#dp[weight_idx][current_weight] : idx번째 추를 올렸을 때, 무게가 w인 경우 이미 만들었으면 True, 만든 적 없으면 False
dp = [[False] * (40001) for _ in range(n+1)]

# 추를 놓을 수 있는 경우의 수
# 1. 왼쪽에 놓는다
# 2. 오른쪽에 놓는다.
# 3. 놓지 않는다.
def find_marble(weight_idx, right_weight, left_weight):
    weight = abs(right_weight - left_weight)

    if dp[weight_idx][weight]:
        return

    dp[weight_idx][weight] = True

    if weight_idx >= n:
        return

    # 오른쪽에 추를 놓는 경우
    find_marble(weight_idx + 1, right_weight + weights[weight_idx], left_weight)
    # 왼쪽에 추를 놓는 경우
    find_marble(weight_idx + 1, right_weight, left_weight + weights[weight_idx])
    # 추를 놓지 않는 경우
    find_marble(weight_idx + 1, right_weight, left_weight)


find_marble(0, 0, 0)


for marble in marbles:
    if dp[n][marble]:
        print('Y', end=" ")
    else:
        print('N', end=" ")
