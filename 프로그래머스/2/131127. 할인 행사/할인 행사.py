def solution(want, number, discount):
    answer = 0
    
    for i in range(0, len(discount) - 9):
        discount_10 = discount[i: i+10]
        buy = True
        
        for j in range(len(want)):
            if discount_10.count(want[j]) != number[j]:
                buy = False
                break
                
        if buy:
            answer +=1
                
    return answer