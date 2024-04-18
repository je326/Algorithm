from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(enumerate(priorities))
    
    while queue:
        l, p = queue.popleft()
        
        if any(p < priority for _, priority in queue):
            queue.append((l, p))
            
        else:
            answer += 1
            if l == location:
                break
                
    return answer
