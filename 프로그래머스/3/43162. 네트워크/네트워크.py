def DFS(n, computers, com, visited):
    visited[com] = True
    for i in range(n):
        if i != com and computers[com][i] == 1:
            if visited[i] == False:
                DFS(n, computers, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            DFS(n, computers, i, visited)
            answer += 1
    
    return answer