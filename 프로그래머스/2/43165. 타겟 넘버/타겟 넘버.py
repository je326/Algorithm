ans = 0

def DFS(numbers, target, idx, value):
    global ans
    
    if (value == target) and (idx == len(numbers)):
        ans += 1
        return
    
    elif idx == len(numbers):
        return

    DFS(numbers, target, idx+1, value+numbers[idx])
    DFS(numbers, target, idx+1, value-numbers[idx])
        
def solution(numbers, target):
    global ans
    ans = 0
    DFS(numbers, target, 0, 0)
    
    return ans