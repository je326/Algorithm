import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        size[x] += size[y]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


T = int(input())
for tc in range(T):

    F = int(input())
    parent = {}
    size = {}

    for i in range(F):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            size[a] = 1

        if b not in parent:
            parent[b] = b
            size[b] = 1

        union(a, b)

        print(size[find(a)])
