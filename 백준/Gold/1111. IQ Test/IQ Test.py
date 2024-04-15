import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

#N이 1일때 여러 수가 올 수 있으므로 A 출력
if N == 1:
    print('A')

#N이 2일때
#두 수가 같다면 같은 수 출력, 다르다면 여러 수가 올 수 있으므로 A 출력
if N == 2:
    if nums[0] == nums[1]:
        print(nums[1])
    else:
        print('A')

#N이 3이상일때 a, b를 구하고 for 문을 돌면서 패턴이 맞는지 검사
#맞다면 다음 값 출력, 다르다면 규칙이 다르므로 B 출력
if N >= 3:
    if nums[1] - nums[0] == 0:
        a = 0
    else :
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
    b = nums[1] - nums[0] * a

    for i in range(N-1):
        next = nums[i] * a + b
    
        if next == nums[i+1]:
            continue
        else:
            print('B')
            exit()
    
    print(nums[-1] * a + b)