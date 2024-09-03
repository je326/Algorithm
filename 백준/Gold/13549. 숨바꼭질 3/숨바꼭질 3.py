import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()

        if v == K: 
            return(time[v])
        
        if 0 < v*2 < limit and not visited[v*2]:
            queue.append(v*2)
            visited[v*2] = True
            time[v*2] = time[v]
            
        if 0 <= v-1 < limit and not visited[v-1]:
            queue.append(v-1)
            visited[v-1] = True
            time[v-1] = time[v] + 1

        if 0 < v+1 < limit and not visited[v+1]:
            queue.append(v+1)
            visited[v+1] = True
            time[v+1] = time[v] + 1

N, K = map(int, input().split())
limit = 100001
visited = [False] * limit
time = [0] * limit

print(bfs(N))
