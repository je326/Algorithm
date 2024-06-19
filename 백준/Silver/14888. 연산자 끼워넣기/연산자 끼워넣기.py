import sys
input = sys.stdin.readline

def calculate(temp, num, op):
    if op == 0:
        return temp + num
    elif op == 1:
        return temp - num
    elif op == 2:
        return temp * num
    elif op == 3:
        return int(temp / num)



def dfs(temp, num_idx, operators_cnt):
    if num_idx == N-1:
        results.append(temp)
        return

    for i in range(4):
        if operators_cnt[i] > 0:
            operators_cnt[i] -= 1
            new_temp = calculate(temp, nums[num_idx + 1], i)
            dfs(new_temp, num_idx+1, operators_cnt)
            operators_cnt[i] += 1

N = int(input())
nums = list(map(int, input().split()))
operators_cnt = list(map(int, input().split()))

results = []

dfs(nums[0], 0, operators_cnt)

print(max(results))
print(min(results))
