def solution(N, stages):
    answer = []
    
    for stage in range(1, N+1):
        user_cnt = 0
        user_total = len([user_stage for user_stage in stages if user_stage >= stage])
        for user_stage in stages:
            if stage == user_stage:
                user_cnt += 1
        answer.append([stage, user_cnt/user_total if user_total > 0 else 0] )
        
        answer = sorted(answer, key = lambda x: (-x[1], x[0]))
        ans = [a[0] for a in answer]
        
    return ans