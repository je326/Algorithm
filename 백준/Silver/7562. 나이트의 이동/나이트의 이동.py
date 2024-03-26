from collections import deque
import sys

input = sys.stdin.readline

def dfs(n, m):
    graph = [[0 for _ in range(l)] for _ in range(l)]

    queue = deque([n])

    while queue:
        n = queue.popleft()

        if n == m:
            return graph[n[0]][n[1]]

        for i in range(len(types)):
            next_n = (n[0] + types[i][0], n[1] + types[i][1])
            if 0 <= next_n[0] < l and 0 <= next_n[1] < l and not graph[next_n[0]][next_n[1]]:
                graph[next_n[0]][next_n[1]] = graph[n[0]][n[1]] + 1
                queue.append(next_n)


types = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
T = int(input())


for tc in range(T):
    l = int(input())
    now_v = tuple(map(int, input().split()))
    move_v = tuple(map(int, input().split()))

    print(dfs(now_v, move_v))

