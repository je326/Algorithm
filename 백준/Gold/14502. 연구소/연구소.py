from collections import deque
import sys
import copy

input = sys.stdin.readline

def bfs():
    queue = deque()
    temp_graph = copy.deepcopy(graph)

    #바이러스 퍼뜨리기
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        v = queue.popleft()

        for i in range(4):
            new_v = (v[0]+dx[i], v[1]+dy[i])
            if 0 <= new_v[0] < N and 0 <= new_v[1] < M and temp_graph[new_v[0]][new_v[1]] == 0:
                temp_graph[new_v[0]][new_v[1]] = 2
                queue.append(new_v)

    #안전영역 세기
    cnt = 0
    global ans
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                cnt += 1

    ans = max(ans, cnt)

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
ans = 0

make_wall(0)
print(ans)
