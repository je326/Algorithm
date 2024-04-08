import sys
input = sys.stdin.readline

#3시 방향 톱니 - idx 2 (오른쪽 톱니바퀴와 맞닿음)
#9시 방향 톱니 - idx 6 (왼쪽 톱니바퀴와 맞닿음)
#N극은 0, S극은 1
#시계 방향은 1, 반시계 방향은 -1

gear = [list(map(int, input().rstrip())) for i in range(4)]
K = int(input()) 
gear_rotation = [list(map(int, input().split())) for i in range(K)]

def rotate_gear(gear_idx, direction):
    if visited[gear_idx]:
        return
    visited[gear_idx] = True 

    # 왼쪽 톱니바퀴 회전 가능성 확인
    if gear_idx > 0 and not visited[gear_idx-1] and gear[gear_idx][6] != gear[gear_idx-1][2]:
        rotate_gear(gear_idx-1, -direction)

    # 오른쪽 톱니바퀴 회전 가능성 확인
    if gear_idx < 3 and not visited[gear_idx+1] and gear[gear_idx][2] != gear[gear_idx+1][6]:
        rotate_gear(gear_idx+1, -direction)

    # 실제 톱니바퀴 회전
    if direction == 1:
        gear[gear_idx] = gear[gear_idx][-1:] + gear[gear_idx][:-1]
    else:
        gear[gear_idx] = gear[gear_idx][1:] + gear[gear_idx][:1]

for gear_num, direction in gear_rotation:
    visited = [False] * 4
    rotate_gear(gear_num-1, direction)

#점수 계산
ans = 0
for i in range(4):
    if gear[i][0] == 1:
        ans += 2**i

print(ans)