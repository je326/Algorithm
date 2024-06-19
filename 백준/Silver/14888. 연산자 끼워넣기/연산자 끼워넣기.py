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
        if temp < 0:
            return -(-temp // num)
        else:
            return temp // num


def dfs(temp, num_idx, operators_visited):
    if num_idx == N-1:
        results.append(temp)
        return

    for i in range(len(operators)):
        if not operators_visited[i]:
            operators_visited[i] = True
            new_temp = calculate(temp, nums[num_idx + 1], operators[i])
            dfs(new_temp, num_idx + 1, operators_visited)
            operators_visited[i] = False


N = int(input())
nums = list(map(int, input().split()))
operators_cnt = list(map(int, input().split()))

#주어진 연산자들을 0, 1, 2, 3으로 +, -, *, //을 표현하여 operators 리스트로 관리
operators = []
for idx, cnt in enumerate(operators_cnt):
    for c in range(cnt):
        operators.append(idx)

operators_visited = [False] * len(operators)
results = []

dfs(nums[0], 0, operators_visited)

print(max(results))
print(min(results))