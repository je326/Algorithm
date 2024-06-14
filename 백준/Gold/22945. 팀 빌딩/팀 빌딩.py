import sys
input = sys.stdin.readline

N = int(input())
users = list(map(int, input().split()))
abilities = []

start, end = 0, N-1
while start < end:
    min_ability = min(users[start], users[end])
    abilities.append(min_ability * (end - start - 1))

    if users[start] < users[end]:
        start += 1
    else:
        end -= 1

print(max(abilities))
