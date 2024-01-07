import sys
read = sys.stdin.readline

N = int(read())

rope = [int(read()) for _ in range(N)]
rope.sort(reverse=True)

ans = []
for i in range(N):
    ans.append(rope[i] * (i+1))

print(max(ans))