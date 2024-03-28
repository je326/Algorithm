from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    want_dict = dict(zip(want, number))
    
    discount_dict = defaultdict(int)
    
    for d in range(10):
        discount_dict[discount[d]] += 1
        answer += check(want_dict, discount_dict)
        
    for i in range(len(discount) - 10):
        if discount_dict[discount[i]] < 1:
            discount_dict.pop(discount[i])
        else:
            discount_dict[discount[i]] -= 1
        
        discount_dict[discount[i + 10]] += 1
        
        answer += check(want_dict, discount_dict)
        
    return answer
        
def check(want_dict, discount_dict):
    return all(want_dict[item] == discount_dict[item] for item in want_dict)
    
    