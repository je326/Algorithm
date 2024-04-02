from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    queue = deque([start])
    visited[start[0][0]][start[0][1]] = 1

    #불의 위치를 찾아서 큐의 앞쪽에 넣어준다.
    #불이 먼저 번져야하기 때문
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                queue.appendleft(((i, j), "fire"))
                visited[i][j] = -1

    while queue:
        v, kind = queue.popleft()

        #상근이가 가장자리에 도착하면 탈출 성공!
        if kind != "fire" and (v[0] == 0 or v[0] == h-1 or v[1] == 0 or v[1] == w-1):
            return visited[v[0]][v[1]]

        for i in range(4):
            new_v = (v[0] + dx[i], v[1] + dy[i])

            if 0 <= new_v[0] < h and 0 <= new_v[1] < w:
                #방문하지 않은 빈공간일 때
                if graph[new_v[0]][new_v[1]] == '.' and visited[new_v[0]][new_v[1]] == 0:
                    #불이면 불 번지게 한다.
                    if kind == "fire":
                        visited[new_v[0]][new_v[1]] = -1
                        queue.append(((new_v[0], new_v[1]), "fire"))
                    #상근이라면 1초 늘려준다.
                    else:
                        visited[new_v[0]][new_v[1]] = visited[v[0]][v[1]] + 1
                        queue.append(((new_v[0], new_v[1]), "person"))

    return "IMPOSSIBLE"


T = int(input())

for tc in range(T):
    w, h = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    #상근이 위치 찾아주고  bfs 시작
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                print(bfs([(i, j), "person"]))
                break
