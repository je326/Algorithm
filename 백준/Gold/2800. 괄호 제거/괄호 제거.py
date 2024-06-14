import itertools
import sys
input = sys.stdin.readline

expression = list(input().rstrip())
brackets = []
pairs = []
for i in range(len(expression)):
    if expression[i] == '(':
        brackets.append(i)
    elif expression[i] == ')':
        pairs.append((brackets.pop(), i))

ans = []
for i in range(len(pairs)):
    combinations = itertools.combinations(pairs, i+1)
    for comb in combinations:
        temp = expression[:]
        for idx in comb:
            temp[idx[0]] = ""
            temp[idx[1]] = ""
        ans.append("".join(temp))

ans = sorted(set(ans))
for a in ans:
    print(a)
