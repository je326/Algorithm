import sys
read = sys.stdin.readline
N = int(read())

for i in range(1, N+1):
    sum = 0
    sum += i
    temp = list(str(i))
    for j in temp:
        sum += int(j)
    if sum == N:
        print(i)
        exit()
print(0)