import sys
input = sys.stdin.readline

def dfs(cnt, idx, eggs):
    global ans
    if idx == N:
        ans = max(ans, cnt)
        return

    if eggs[idx][0] <= 0:
        dfs(cnt, idx + 1, eggs)
        return

    hit = False
    for i in range(N):
        if i != idx and eggs[i][0] > 0:
            hit = True
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]

            next_cnt = cnt

            if eggs[idx][0] <= 0:
                next_cnt += 1

            if eggs[i][0] <= 0:
                next_cnt += 1

            dfs(next_cnt, idx+1, eggs)

            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

    if not hit:
        dfs(cnt, idx+1, eggs)


N = int(input())
ans = 0
eggs = [list(map(int, input().split())) for _ in range(N)]

dfs(0, 0,  eggs)
print(ans)
