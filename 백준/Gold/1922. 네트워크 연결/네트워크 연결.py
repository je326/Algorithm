import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

#부모 테이블 초기화
parent = [i for i in range(N+1)]

def find(v):
    if parent[v] != v:
        return find(parent[v])
    return parent[v]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


#간선 정보 저장하기
edges = []
for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, (a, b)))

#비용을 기준으로 오름차순 정렬
edges.sort()

total = 0
for i in range(M):
    cost, edge = edges[i]
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        total += cost

print(total)