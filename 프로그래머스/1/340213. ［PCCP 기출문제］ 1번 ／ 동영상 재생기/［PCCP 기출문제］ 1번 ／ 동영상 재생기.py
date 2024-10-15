def solution(video_len, pos, op_start, op_end, commands):
    
    def skip_op(t):
        if op_start <= t <= op_end:
            return op_end
        return t
    
    def str_to_sec(s):
        mm, ss = map(int, s.split(':'))
        return mm*60 + ss
    
    def sec_to_str(t):
        mm, ss = divmod(t, 60)
        return f'{mm:02d}:{ss:02d}'
        
    video_len, pos, op_start, op_end = map(str_to_sec, [video_len, pos, op_start, op_end])
    
    pos = skip_op(pos)
    for command in commands:
        if command == "next":
            pos = min(video_len, pos+10)
        
        else: pos = max(0, pos-10)
        pos = skip_op(pos)
        
    answer = sec_to_str(pos)
    return answer