import sys
read = sys.stdin.readline

N = int(read())
tips = [int(read()) for _ in range(N)]

tips.sort(reverse=True)

sum = 0
index = 0

for t in tips:
    sum += max(t - tips.index(t, index, len(tips)), 0)
    index += 1

print(sum)
