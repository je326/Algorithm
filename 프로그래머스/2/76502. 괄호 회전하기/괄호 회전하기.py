def solution(s):
    cnt = 0
    
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        
        while True:
            length = len(temp)
            temp = temp.replace("{}", '')
            temp = temp.replace("[]", '')
            temp = temp.replace("()", '')
        
            if len(temp) == 0:
                cnt += 1
                break
            if length == len(temp):
                break
    return cnt
    