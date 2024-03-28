import sys
input = sys.stdin.readline

def check():
    if max == 0:
        print("SAD")
    else:
        print(max)
        print(cnt)

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

max = 0
sum = 0

for i in range(X):
    sum += visitors[i]
max = sum
cnt = 1

if N == X:
    check()
    exit()

for i in range(N - X):
    sum -= visitors[i]
    sum += visitors[i + X]

    if sum > max:
        max = sum
        cnt = 1
        continue

    if sum == max:
        cnt += 1

check()


