import sys
read = sys.stdin.readline

N = int(read())
tree = list(map(int, read().split()))
delete = int(read())

#노드 삭제하기
def dfs(delete_node):
    tree[delete_node] = -10
    for i in range(N):
        if tree[i] == delete_node:
            dfs(i)

dfs(delete)

#리프 노드 세기
ans = 0
for i in range(len(tree)):
    if tree[i] != -10 and i not in tree:
        ans += 1
print(ans)