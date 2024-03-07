from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    Q = deque([(0, 0)])

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y]+1
                Q.append((nx,ny))

    answer = maps[len(maps)-1][len(maps[0])-1]

    if answer == 1:
        answer = -1
        
    return answer